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
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework.renderers import JSONRenderer
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
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger/v1/swagger.json', SpectacularAPIView.as_view(renderer_classes=[JSONRenderer]), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/', include(router.urls)),

    path('api/v1/register/', UserRegistrationView.as_view(), name='user_registration'),

    path('api/v1-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
