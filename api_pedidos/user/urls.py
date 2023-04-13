from rest_framework import routers
from user.views import *

app_name = 'user'

router = routers.DefaultRouter()

router.register(r'api/login', LoginViewSet, basename='Login'),
router.register(r'api/signup', UserViewSet, basename='Signup')
#router.register(r'api/pedidos/<int:pk>/', PedidoDetail, basename='pedido_retrieve_update_destroy')

urlpatterns = router.urls