from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import JobPosting, Applicant, Application
from .serializers import JobPostingSerializer, ApplicantSerializer, ApplicationSerializer

@extend_schema_view(
    list=extend_schema(tags=['JobPosting']),
    retrieve=extend_schema(tags=['JobPosting']),
    create=extend_schema(tags=['JobPosting']),
    update=extend_schema(tags=['JobPosting']),
    partial_update=extend_schema(tags=['JobPosting']),
    destroy=extend_schema(tags=['JobPosting']),
)
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all().order_by('-created_at')
    serializer_class = JobPostingSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@extend_schema_view(
    list=extend_schema(tags=['Applicant']),
    retrieve=extend_schema(tags=['Applicant']),
    create=extend_schema(tags=['Applicant']),
    update=extend_schema(tags=['Applicant']),
    partial_update=extend_schema(tags=['Applicant']),
    destroy=extend_schema(tags=['Applicant']),
)
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


@extend_schema_view(
    list=extend_schema(tags=['Application']),
    retrieve=extend_schema(tags=['Application']),
    create=extend_schema(tags=['Application']),
    update=extend_schema(tags=['Application']),
    partial_update=extend_schema(tags=['Application']),
    destroy=extend_schema(tags=['Application']),
)
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
