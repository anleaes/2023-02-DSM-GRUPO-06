from django.shortcuts import render
from .models import Usuarios
from rest_framework import viewsets
from .serializer import UsuarioSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer  
    