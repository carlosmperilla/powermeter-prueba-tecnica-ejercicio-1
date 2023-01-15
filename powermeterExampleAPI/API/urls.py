from django.urls import include, path
from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import MedidorViewSet, MedicionViewSet

router = routers.DefaultRouter()
router.register(r'Medidores', MedidorViewSet)
router.register(r'Mediciones', MedicionViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Powermet API v1",
      default_version='v1',
      description="API v1, permite obtener y gestionar información de medidores.",
      terms_of_service="Indefinido",
      contact=openapi.Contact(email="carlosperillaprogramacion@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]