from django.db import models
from ninetails_utils.abstract_models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import random

class Course(models.Model):   
    title = models.CharField(
        _('Course Name'),
        help_text=_('Enter The Course Title'),
        max_length=255
    )
    description = models.TextField(
        _('Course Description'),
        help_text=_('Enter The Course Description'),
        blank=True, null=True
    )
    keywords = models.TextField(
        verbose_name=_("SEO keys"),
        help_text=_("eg: mathematics,BusinessStudies,Management"),
        blank=True,null=True
    )
    school = models.ForeignKey(
        "school_management.School",verbose_name="School",
        related_name="courses",on_delete=models.SET_NULL,
        blank=True,null=True
    )
    teacher = models.ForeignKey(
        "school_management.Teacher",verbose_name="Teacher",
        related_name="courses",on_delete=models.SET_NULL,
        blank=True,null=True
    )
    monthly_rate = models.PositiveIntegerField(
        verbose_name=_("Monthly Rate"),
    )
    yearly_rate = models.PositiveIntegerField(
        verbose_name=_("Yearly Rate"),
    )
    promo_video_link = models.URLField(
        verbose_name=_("Promotion Link"),
    )

    class Status(models.TextChoices):
        PUBLISHED = 'P', _('PUBLISHED')
        NOT_PUBLISHED = 'NP', _('NOT PUBLISHED')
    
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.NOT_PUBLISHED,
    )

        
    def __str__(self) -> str:
        return f"{self.title}"

        
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Registered Courses"

