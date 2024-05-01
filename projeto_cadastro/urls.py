from django.urls import path
from app_bigshow import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    # usuario.com
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
