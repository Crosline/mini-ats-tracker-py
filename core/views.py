from rest_framework import viewsets, permissions, generics, response, status
from drf_spectacular.utils import extend_schema_view, extend_schema
from django.contrib.auth.models import User
from .models import JobPosting, Applicant, Application
from .serializers import JobPostingSerializer, ApplicantSerializer, ApplicationSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# --- Registration ViewSet ---
@extend_schema(tags=['Registration'])
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        res = response.Response(data, status=status.HTTP_201_CREATED)
        res.set_cookie('refresh_token', str(refresh.access_token), httponly=True)

        return res

# --- Core Model ViewSets ---
@extend_schema(tags=['JobPosting'])
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all().order_by('-created_at')
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def get_queryset(self):
        return JobPosting.objects.all().order_by('-created_at')


@extend_schema(tags=['Applicant'])
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['Application'])
class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Application.objects.filter(job__created_by=self.request.user).order_by('-job__updated_at')
        job_id = self.request.query_params.get('job_id')
        applicant_name = self.request.query_params.get('applicant')

        if job_id is not None:
            queryset = queryset.filter(job__id=job_id)

        if applicant_name is not None:
            queryset = queryset.filter(applicant__name__icontains=applicant_name)

        return queryset

    def perform_create(self, serializer):
        serializer.save()