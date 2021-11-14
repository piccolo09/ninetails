from django.contrib import admin
from .models import Course
# Register your models here.


@admin.register(Course)
class CourseManagementAdmin(admin.ModelAdmin):
    list_display = ('title','description','school','teacher','status')
    # readonly_fields = ('created_date', 'updated_date','updated_by','created_by')