from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_unidade', criar_unidade, name='cadastrar_unidade'),
    path('listar_unidade', listar_unidade, name='listar_unidade'),
    path('editar_unidade/<int:id>', editar_unidade, name='editar_unidade'),
    path('visualizar_unidade/<int:id>', visualizar_unidade, name='visualizar_unidade'),
]
