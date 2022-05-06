from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.perfil, name='perfil'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),

]