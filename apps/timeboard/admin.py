from django.contrib import admin
from apps.timeboard.models import ProductivityDaily, ProductivityType, Activity


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0
    fields = ("productivity_type", "hours")
    verbose_name = "activity"
    verbose_name_plural = "activities"

@admin.register(ProductivityDaily)
class ProductivityDailyAdmin(admin.ModelAdmin):
    list_display = ("id", "score", "date")
    search_fields = ("score",)
    list_filter = ("date",)
    ordering = ("-date",)
    inlines = (ActivityInline,)
    readonly_fields = ("score",)
    
    
    def save_formset(self, request, form, formset, change):
        formset.save()
        activity_scores = []
        total_productivity_factor = sum(form.instance.daily_activities.values_list("productivity_type__productivity_factor", flat=True))
        for activity in form.instance.daily_activities.all():
            activity_scores.append(activity.hours * activity.productivity_type.productivity_factor)

        form.instance.score = sum(activity_scores)/total_productivity_factor
        form.instance.save()


@admin.register(ProductivityType)
class ProductivityTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "productivity_factor", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "productivity_daily", "productivity_type", "hours", "created_at", "updated_at")
    search_fields = ("productivity_daily__score", "productivity_type__name")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)