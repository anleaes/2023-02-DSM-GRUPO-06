from django.shortcuts import render
from .models import Solicitacao
from rest_framework import viewsets
from .serializer import SolicitacaoSerializer

# Create your views here.

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer  
