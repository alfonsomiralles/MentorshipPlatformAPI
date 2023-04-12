from rest_framework import serializers
from .models import Mentor, Project, Mentorship

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    mentors = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'mentors')

    def get_mentors(self, obj):
        mentorships = Mentorship.objects.filter(project=obj)
        mentors = [mentorship.mentor for mentorship in mentorships]
        return MentorSerializer(mentors, many=True).data    

class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'