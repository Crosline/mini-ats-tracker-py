from rest_framework import viewsets
from .models import JobPosting, Applicant, Application
from .serializers import JobPostingSerializer, ApplicantSerializer, ApplicationSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all().order_by('-created_at')
    serializer_class = JobPostingSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.all()
        job_id = self.request.query_params.get('job_id')
        applicant_name = self.request.query_params.get('applicant')

        if job_id is not None:
            queryset = queryset.filter(job__id=job_id)

        if applicant_name is not None:
            queryset = queryset.filter(applicant__name__icontains=applicant_name)

        return queryset

    def perform_create(self, serializer):
        serializer.save()

