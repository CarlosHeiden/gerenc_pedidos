from rest_framework import routers
from user.views import *

app_name = 'user'

router = routers.DefaultRouter()

router.register(r'api/signup', UserViewSet, basename='Signup')


urlpatterns = router.urls