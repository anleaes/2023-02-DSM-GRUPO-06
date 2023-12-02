from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orgãos'

router = routers.DefaultRouter()
router.register('', views.OrgaoViewSet, basename='orgãos')

urlpatterns = [
    path('', include(router.urls) )
]