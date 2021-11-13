from django.db import models
from ninetails_utils.abstract_models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()
import random

class Student(BaseModel):

    first_name = models.CharField(
        _('First Name'),
        help_text=_('First Name of Student'),
        max_length=255)
    
    last_name = models.CharField(
        _('Last Name'),
        help_text=_('Last Name of Student'),
        max_length=255,
        blank=True,null=True)

    mobile = models.CharField(
        verbose_name=_("Contact Phone No."),
        max_length=15)

    email = models.EmailField(
        verbose_name=_("Contact Email"),
        help_text=_("Official Email address of student")
    )
    school = models.ForeignKey(
        "School",verbose_name="Linked School",
        related_name="students",on_delete=models.SET_NULL,
        blank=True,null=True)

    related_user = models.OneToOneField(
        User,
        verbose_name=_("Related user"),
        on_delete=models.RESTRICT,
        help_text=_("User responsible for school profile"),
        blank=True,null=True
    )
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.name