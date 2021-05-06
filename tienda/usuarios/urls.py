from rest_framework import routers
from . import views
from .views import *
from django.urls import path


router = routers.SimpleRouter()
router.register(r'v1/create/user', createUser, basename="crearusuario")

urlpatterns = [
  path('<int:pk>', views.createUser.as_view)
] + router.urls




