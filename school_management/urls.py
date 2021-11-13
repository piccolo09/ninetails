from rest_framework import routers, urlpatterns

from school_management.models import school
from .views import SchoolViewset
schoolrouter =  routers.DefaultRouter()

schoolrouter.register(prefix="school",viewset=SchoolViewset,basename="")

urlpatterns = [ ]

urlpatterns += schoolrouter.urls