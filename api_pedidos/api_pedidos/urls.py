
from django.contrib import admin
from django.urls import path, include
from pedidos.urls import router as pedidos_router
from user.urls import router as users_router
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include((pedidos_router.urls, 'pedidos'), namespace='pedidos')),
    path('users/', include((users_router.urls, 'users'), namespace= 'users')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 ]  
