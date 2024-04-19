from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_gerente', criar_gerente, name='cadastrar_gerente'),
    path('listar_gerente', listar_gerente, name='listar_gerente'),
    path('editar_gerente/<int:id>', editar_gerente, name='editar_gerente'),
    path('visualizar_gerente/<int:id>', visualizar_gerente, name='visualizar_gerente'),       
]
