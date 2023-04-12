from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Mentor, Project, Mentorship
from .serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
