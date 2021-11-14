from rest_framework import viewsets
# from .serializers import Serializer
from .models import Course




class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    # serializer_class = Serializer