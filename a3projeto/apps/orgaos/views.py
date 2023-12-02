from django.shortcuts import render
from .models import Orgao
from rest_framework import viewsets
from .serializer import OrgaoSerializer


# Create your views here.

class OrgaoViewSet(viewsets.ModelViewSet):
    queryset = Orgao.objects.all()
    serializer_class = OrgaoSerializer 
