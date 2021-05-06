
from rest_framework import routers
from . import views
from .views import *
from django.urls import path


router = routers.SimpleRouter()
router.register(r'v1/create/area', CreateArea, basename="crear-producto")

urlpatterns = [

] + router.urls
