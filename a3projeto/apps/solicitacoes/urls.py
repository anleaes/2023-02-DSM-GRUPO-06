from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'solicitacoes'

router = routers.DefaultRouter()
router.register('', views.SolicitacaoViewSet, basename='solicitacoes')

urlpatterns = [
    path('', include(router.urls) )
]