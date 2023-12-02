from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'materiaisitens'

router = routers.DefaultRouter()
router.register('', views.MateriaisitensViewSet, basename='materiaisitens')

urlpatterns = [
    path('', include(router.urls) )
]