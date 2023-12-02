from django.shortcuts import render
from .models import Material
from rest_framework import viewsets
from .serializer import MaterialSerializer

# Create your views here.

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer  
