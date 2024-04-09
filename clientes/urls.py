from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_crianca', criar_crianca, name='cadastrar_crianca'),
    path('listar_criancas', listar_crianca, name='listar_criancas'),
    path('editar_crianca/<int:id>', editar_crianca, name='editar_crianca'),
    path('visualizar_crianca/<int:id>', visualizar_crianca, name='visualizar_crianca'),    
]
