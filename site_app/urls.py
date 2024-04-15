from django.urls import path
from .views import home, delete, delpesquisa, confirma, deletar, atualiza, delatualiza, atualizar, cadastro, update, pesquisar, pesquisa

urlpatterns = [
    path('', home, name="home"),
    path('cadastro', cadastro, name="cadastro"),
    path('delete/', delete, name="delete"),
    path('confirma/<int:id>', confirma, name="confirma"),
    path('deletar/<int:id>', deletar, name="deletar"),
    path('atualiza/', atualiza, name="atualiza"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('update/<int:id>', update, name="update"),
    path('pesquisar', pesquisar, name="pesquisar"),
    path('pesquisa', pesquisa, name="pesquisa"),
    path('delpesquisa', delpesquisa, name="delpesquisa"),
    path('delatualiza', delatualiza, name="delatualiza"),

]
