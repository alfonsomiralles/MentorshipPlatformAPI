from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project, Mentor
import json

class ProjectTestCase(APITestCase):

    def setUp(self):
        self.project1 = Project.objects.create(name="Project 1")
        self.project2 = Project.objects.create(name="Project 2")
        self.mentor1 = Mentor.objects.create(name="Mentor 1")
        self.mentor2 = Mentor.objects.create(name="Mentor 2")

    def test_project_list(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_project_detail(self):
        response = self.client.get(reverse('project-detail', kwargs={'pk': self.project1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.project1.name)

    def test_project_create(self):
        data = {'name': 'New Project'}
        response = self.client.post(reverse('project-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 3)

    def test_project_update(self):
        data = {'name': 'Updated Project', 'mentors': [self.mentor2.pk]}
        json_data = json.dumps(data) 
        response = self.client.put(reverse('project-detail', kwargs={'pk': self.project1.pk}), json_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(pk=self.project1.pk)
        self.assertEqual(project.name, 'Updated Project')
        self.assertEqual(list(project.mentors.all()), [self.mentor2])   

    def test_project_delete(self):
        response = self.client.delete(reverse('project-detail', kwargs={'pk': self.project1.pk}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)     