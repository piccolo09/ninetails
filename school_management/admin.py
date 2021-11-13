from django.contrib import admin
from .models import School,Teacher,Student
# Register your models here.


@admin.register(School)
class SchoolManagementAdmin(admin.ModelAdmin):
    list_display = ('name','owner','promo', 'mobile','student_count','teacher_count')
    readonly_fields = ('created_date', 'updated_date','updated_by','created_by')
    search_fields = ['name','country']
    list_filter = ['country']


@admin.register(Teacher)
class TeacherManagementAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','mobile', 'email','school')
    readonly_fields = ('created_date', 'updated_date','updated_by','created_by')
    search_fields = ['first_name','school__name','last_name']
    list_filter = ['school',]


@admin.register(Student)
class StudentManagementAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','mobile', 'email','school')
    readonly_fields = ('created_date', 'updated_date','updated_by','created_by')
    search_fields = ['first_name','school__name','last_name']
    list_filter = ['school',]



