from rest_framework import serializers
from .models import Mentor, Project, Mentorship

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    mentors = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Mentor.objects.all())

    class Meta:
        model = Project
        fields = '__all__'

    def get_mentors(self, obj):
        active_mentorships = Mentorship.objects.filter(project=obj, status='active')
        active_mentors = [mentorship.mentor for mentorship in active_mentorships]
        return [{'id': mentor.id, **MentorSerializer(mentor, context=self.context).data} for mentor in active_mentors]

    def get_mentor_names(self, obj):
        mentors = self.get_mentors(obj)
        return [mentor['name'] for mentor in mentors]

    mentor_names = serializers.SerializerMethodField(source='get_mentors')    

class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'