from django.db import models
from ninetails_utils.abstract_models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()
import random


class School(BaseModel):
    name = models.CharField(
        _('School Name'),
        help_text=_('Official registed name of school'),
        max_length=255)

    mobile = models.CharField(
        verbose_name=_("Contact Phone No."),
        max_length=15)

    email = models.EmailField(
        verbose_name=_("Contact Email"),
        help_text=_("Official Email address of school")
    )

    keywords = models.TextField(
        verbose_name=_("SEO keys"),
        help_text=_("eg: mathematics,BusinessStudies,Management"),
        blank=True,null=True
    )
    promo = models.URLField(
        verbose_name=_("Promotion Link"),
    )
    owner = models.ForeignKey(
        User,
        verbose_name=_("Owner user"),
        on_delete=models.RESTRICT,
        help_text=_("User responsible for school profile")
    )

    country = models.CharField(
        _('Country'),
        max_length=255)


    short_intro = models.TextField(blank=True,null=True)

    long_intro = models.TextField(blank=True,null=True)

    # def clean(self) -> None:
    #     if self.pk:
    #         pass
    #     return super().clean()
    
    def __str__(self) -> str:
        return f"{self.name} | {self.owner}"

    @property
    def student_count(self):
        """
            will check students and return count of students
        """
        return random.randint(10,2347)
    
    @property
    def teacher_count(self):
        """
            will check students and return count of students
        """
        return self.teachers.count()
    
    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Registered Schools"
