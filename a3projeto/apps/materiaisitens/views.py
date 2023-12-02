from django.shortcuts import render
from .models import Materiaisitens
from rest_framework import viewsets
from .serializer import MateriaisitensSerializer

# Create your views here.
class MateriaisitensViewSet(viewsets.ModelViewSet):
    queryset = Materiaisitens.objects.all()
    serializer_class = MateriaisitensSerializer  
