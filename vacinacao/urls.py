from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_vacinacao', criar_vacinacao, name='cadastrar_vacinacao'),
    path('listar_vacinacao', listar_vacinacao, name='listar_vacinacao'),
    path('editar_vacinacao/<int:id>', editar_vacinacao, name='editar_vacinacao'),
    path('visualizar_vacinacao/<int:id>', visualizar_vacinacao, name='visualizar_vacinacao'),
]
