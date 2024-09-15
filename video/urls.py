from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/schema/',
         SpectacularAPIView.as_view(),
         name='schema'),

    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
