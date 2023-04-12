from django.urls import path, include
from .views import MentorViewSet, ProjectViewSet, MentorshipViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'mentors', MentorViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'mentorships', MentorshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
