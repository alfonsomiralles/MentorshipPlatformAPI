from django.contrib import admin
from .models import Mentor, Project, Mentorship
# Register your models here.


admin.site.register(Mentor)
admin.site.register(Project)
admin.site.register(Mentorship)