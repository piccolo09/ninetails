from django.db.models import fields
from rest_framework import serializers
from .models import School
from school_management import models


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"
