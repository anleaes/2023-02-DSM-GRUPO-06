"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('localizacoes/', include('localizacoes.urls', namespace='localizacoes')),
    path('solicitacoes/', include('solicitacoes.urls', namespace='solicitacoes')),
    path('avaliacoes/', include('avaliacoes.urls', namespace='avaliacoes')),
    path('fornecedores/', include('fornecedores.urls', namespace='fornecedores')),
    path('orgaos/', include('orgaos.urls', namespace='orgaos')),
    path('servicos/', include('servicos.urls', namespace='servicos')),
    path('materiais/', include('materiais.urls', namespace='materiais')),
    path('materiaisitens/', include('materiaisitens.urls', namespace='materiaisitens')),
]
