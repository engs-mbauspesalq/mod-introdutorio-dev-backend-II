from django.contrib import admin
from django.urls import path, include
from restaurantes.views import RestauranteViewSet, PratoViewSet, ListaPratosDeUmRestauranteView, ListandoTagsView, ListaRestaurantesView, ListaPratosView, UserViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
   openapi.Info(
      title="API de restaurantes e pratos",
      default_version='v1',
      description="Provedor local de restaurantes e pratos desenvolvida pela Alura para o curso de React",
      terms_of_service="#",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename="User")
router.register('restaurantes', RestauranteViewSet, basename='Restaurantes')
router.register('pratos', PratoViewSet, basename='Pratos')

urlpatterns = [
   path('admin-api/', admin.site.urls),
   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/v1/restaurantes/', ListaRestaurantesView.as_view() ),
   path('api/v1/pratos/', ListaPratosView.as_view() ),
   path('api/v2/', include(router.urls) ),
   path('api/v1/restaurantes/<int:pk>/pratos/', ListaPratosDeUmRestauranteView.as_view() ),
   path('api/v2/tags/', ListandoTagsView.as_view() ),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
