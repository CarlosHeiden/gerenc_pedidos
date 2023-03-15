from rest_framework.routers import DefaultRouter
from pedidos.views import PedidoViewSet

app_name = 'pedidos'

router = DefaultRouter(trailing_slash= False)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = router.urls