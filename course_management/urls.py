from rest_framework import routers, urlpatterns
from course_management.models import course
from .views import CourseViewset
courserouter =  routers.DefaultRouter()




courserouter.register(prefix="course",viewset=CourseViewset,basename="")



urlpatterns = [ ]

urlpatterns += courserouter.urls