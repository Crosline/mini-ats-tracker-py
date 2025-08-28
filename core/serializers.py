from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Applicant, Application, JobPosting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'name', 'email', 'resume']

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'title', 'description', 'location', 'created_by', 'created_at']
        read_only_fields = ['created_at', 'created_by']

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)
    job = JobPostingSerializer(read_only=True)

    applicant_id = serializers.PrimaryKeyRelatedField(
        queryset=Applicant.objects.all(), source='applicant', write_only=True
    )
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=JobPosting.objects.all(), source='job', write_only=True
    )
    
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['applied_at']