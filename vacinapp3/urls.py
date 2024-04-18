"""
URL configuration for vacinapp3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacina/', include('vacina.urls')),
    path('vacinacao/', include('vacinacao.urls')),
    path('crianca/', include('clientes.urls')),
    path('responsavel/', include('clientes.urls')),
    path('unidade/', include('unidade_saude.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),    
    # path('', TemplateView.as_view(template_name="vacina/listar_vacinas.html"), name="listar_vacinas"),
]
