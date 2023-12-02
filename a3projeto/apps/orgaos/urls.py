from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orgaos'

router = routers.DefaultRouter()
router.register('', views.OrgaoViewSet, basename='orgaos')

urlpatterns = [
    path('', include(router.urls) )
]