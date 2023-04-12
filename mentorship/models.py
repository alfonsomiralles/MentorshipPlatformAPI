from django.db import models

# Create your models here.

class Mentor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-binary'),
        ('O', 'Other'),
    ]
    email = models.EmailField()
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mentorship(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deleted', 'Deleted'),
    ]
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.mentor.id} - {self.project.id}"