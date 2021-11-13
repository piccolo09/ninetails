from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SchoolSerializer
from .models import School




class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
# Create your views here.
