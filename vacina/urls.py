from django.urls import path
from .views import *

urlpatterns = [
    path('vacinahome/', criar_vacina, name='criar_vacina'),    
    path('listar_vacinas/', listar_vacinas, name='listar_vacinas'),
    path('editar_vacina/<int:id>', editar_vacina, name='editar_vacina'),
    path('visualizarvacina/<int:id>', visualizar_vacina, name='visualizar_vacina'),

    #urls para calendário de vacinação
    path('nova_vacina/', add_vacina_calendario, name='nova_vacina'),
    path('calendario/', ver_calendario, name='calendario')
]
