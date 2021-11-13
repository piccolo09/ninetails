from django.db.models import fields
from rest_framework import serializers
from school_management import models
from .models import School,Teacher,Student


class TeacherViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ('id','first_name','last_name','email','mobile')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id','first_name','last_name','email','mobile','school')



class SchoolSerializer(serializers.ModelSerializer):
    
    teachers = TeacherViewSerializer(many=True,read_only=True)
    
    class Meta:
        model = School
        fields = ('name','owner','promo', 'mobile','email','country','teachers')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','first_name','last_name','email','mobile','school')