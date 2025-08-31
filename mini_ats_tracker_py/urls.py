"""
URL configuration for mini_ats_tracker_py project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
import mini_ats_tracker_py.openapi_extensions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views import ApplicantViewSet, ApplicationViewSet, JobPostingViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'jobs', JobPostingViewSet, basename='jobposting')
router.register(r'applicants', ApplicantViewSet, basename='applicant')
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include("core.urls")),
    
    path('', include(router.urls)),
    path('api/v1/', include(router.urls)),

    path('api/v1/register/', UserRegistrationView.as_view(), name='user_registration'),

    path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
