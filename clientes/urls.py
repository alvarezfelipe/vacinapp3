from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_crianca', criar_crianca, name='cadastrar_crianca'),
    path('listar_criancas', listar_crianca, name='listar_criancas'),
    path('editar_crianca/<int:id>', editar_crianca, name='editar_crianca'),
    path('visualizar_crianca/<int:id>', visualizar_crianca, name='visualizar_crianca'),
    path('cadastrar_resp', criar_resp, name='cadastrar_resp'),
    path('listar_resp', listar_resp, name='listar_resp'),
    path('editar_resp/<int:id>', editar_resp, name='editar_resp'),
    path('visualizar_resp/<int:id>', visualizar_resp, name='visualizar_resp'),    
]
