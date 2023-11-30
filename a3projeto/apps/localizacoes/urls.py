from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'localizacoes'

router = routers.DefaultRouter()
router.register('', views.LocalizacaoViewSet, basename='localizacoes')

urlpatterns = [
    path('', include(router.urls) )
]
