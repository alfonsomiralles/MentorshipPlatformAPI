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
        fields = '__all__'

    def get_mentors(self, obj):
        active_mentorships = Mentorship.objects.filter(project=obj, status='active')
        active_mentors = [mentorship.mentor for mentorship in active_mentorships]
        return MentorSerializer(active_mentors, many=True, read_only=True, context=self.context).data    

class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'