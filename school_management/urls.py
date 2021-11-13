from rest_framework import routers, urlpatterns

from school_management.models import school
from .views import SchoolViewset,TeacherViewset,StudentViewset
schoolrouter =  routers.DefaultRouter()




schoolrouter.register(prefix="school",viewset=SchoolViewset,basename="")
schoolrouter.register(prefix="teacher",viewset=TeacherViewset,basename="")
schoolrouter.register(prefix="student",viewset=StudentViewset,basename="")



urlpatterns = [ ]

urlpatterns += schoolrouter.urls