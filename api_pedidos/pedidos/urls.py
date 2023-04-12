from rest_framework import routers
from . import views
from pedidos.views import *

app_name = 'pedidos'

router = routers.DefaultRouter()

router.register(r'api/pedidos', PedidoViewSet, basename='pedido_list_create')
#router.register(r'api/pedidos/<int:pk>/', PedidoDetail, basename='pedido_retrieve_update_destroy')

urlpatterns = router.urls