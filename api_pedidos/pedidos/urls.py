from rest_framework import routers
from pedidos.views import PedidoViewSet

app_name = 'pedidos'

router = routers.DefaultRouter()

router.register(r'api/pedidos', PedidoViewSet, basename='Pedidos')

urlpatterns = router.urls