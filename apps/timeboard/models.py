import datetime
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    
    class Meta:
        abstract = True


class ProductivityDaily(BaseModel):
    score = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, verbose_name="score")
    date = models.DateField(verbose_name="date", default=datetime.date.today)

    class Meta:
        verbose_name = "Productivity Daily"
        verbose_name_plural = "Productivity Daily"


    def __str__(self):
        return super().__str__()


class ProductivityType(BaseModel):
    name = models.CharField(max_length=150, verbose_name="name")
    productivity_factor = models.PositiveSmallIntegerField(default=0, verbose_name="productivity factor")
    
    class Meta:
        verbose_name = "Productivity Type"
        verbose_name_plural = "Productivity Types"


    def __str__(self):
        return self.name


class Activity(BaseModel):
    productivity_daily = models.ForeignKey(
        ProductivityDaily, 
        on_delete=models.CASCADE, 
        related_name="daily_activities", 
        verbose_name="productivity details",
    )
    productivity_type = models.ForeignKey(
        ProductivityType,
        on_delete=models.CASCADE,
        related_name="activity_types",
        verbose_name="productivity type",
    )

    hours = models.PositiveSmallIntegerField(default=0, verbose_name="hours")

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"


    def __str__(self):
        return super().__str__()
