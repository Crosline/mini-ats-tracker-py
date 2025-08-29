from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Applicant, Application, JobPosting

# --- User Registration Serializer ---
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# --- User Serializer ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# --- Core Model Serializers ---
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'name', 'email']

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