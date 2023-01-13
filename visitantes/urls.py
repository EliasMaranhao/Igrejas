from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('busca/<int:visitante_id>', views.busca, name='busca')
]