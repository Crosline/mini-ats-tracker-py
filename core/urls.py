from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.renderers import JSONRenderer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/v1/swagger.json', SpectacularAPIView.as_view(renderer_classes=[JSONRenderer]), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('api/v1-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
