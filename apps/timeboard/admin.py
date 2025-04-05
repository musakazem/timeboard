from django.contrib import admin
from admin_extra_buttons.api import ExtraButtonsMixin, button

from apps.timeboard.models import ProductivityDaily, ProductivityType, Activity
from apps.timeboard.plots import plot_productivity_chart


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0
    fields = ("productivity_type", "hours")
    verbose_name = "activity"
    verbose_name_plural = "activities"

@admin.register(ProductivityDaily)
class ProductivityDailyAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ("id", "score", "date")
    search_fields = ("score",)
    list_filter = ("date",)
    ordering = ("-date",)
    inlines = (ActivityInline,)
    readonly_fields = ("score",)
    
    
    def save_formset(self, request, form, formset, change):
        IDEAL_PRODUCTIVITY_HOURS = 8
        formset.save()
        activity_scores = []
        total_productivity_factor = sum(form.instance.daily_activities.values_list("productivity_type__productivity_factor", flat=True))
        for activity in form.instance.daily_activities.all():
            activity_scores.append(activity.hours * activity.productivity_type.productivity_factor)

        form.instance.score = sum(activity_scores)/IDEAL_PRODUCTIVITY_HOURS
        form.instance.save()

    @button(html_attrs={"class": "aeb-green"})
    def this_week(self, request):
        plot_productivity_chart(7)

    @button(html_attrs={"style": "background-color:#1E90FF;color:#FFFFFF;"})
    def this_month(self, request):
        plot_productivity_chart(30)


@admin.register(ProductivityType)
class ProductivityTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "productivity_factor", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    list_editable = ("productivity_factor",)


# @admin.register(Activity)
# class ActivityAdmin(admin.ModelAdmin):
#     list_display = ("id", "productivity_daily", "productivity_type", "hours", "created_at", "updated_at")
#     search_fields = ("productivity_daily__score", "productivity_type__name")
#     list_filter = ("created_at", "updated_at")
#     ordering = ("-created_at",)
