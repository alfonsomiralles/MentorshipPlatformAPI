from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from rest_framework import viewsets
from .models import Mentor, Project, Mentorship
from .serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer

class MentorFilter(filters.FilterSet):
    class Meta:
        model = Mentor
        fields = ['name', 'email']

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = MentorFilter
    search_fields = ['name', 'email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        mentor_id = serializer.data['id']
        return HttpResponseRedirect(reverse('mentor-detail', kwargs={'pk': mentor_id}))

class ProjectFilter(filters.FilterSet):
    class Meta:
        model = Project
        fields = ['name']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ProjectFilter
    search_fields = ['name']

class MentorshipFilter(filters.FilterSet):
    class Meta:
        model = Mentorship
        fields = ['status']

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'put', 'patch']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MentorshipFilter
