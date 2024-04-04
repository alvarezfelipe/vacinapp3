from django.urls import path
from .views import *

urlpatterns = [
    path('vacinahome/', criar_vacina, name='criar_vacina'),
    path('hello/', teste, name='hello'),
    path('listar_vacinas/', listar_vacinas, name='listar_vacinas'),
    path('editar_vacina/<int:id>', editar_vacina, name='editar_vacina'),
    path('visualizar_vacina/<int:id>', visualizar_vacina, name='visualizar_vacina'),
]
