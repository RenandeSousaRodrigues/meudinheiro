from django.urls import path

app_name = 'geral'

from geral import views

urlpatterns=[
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('categorias/', views.lista_categorias, name='Lista_categorias'),
    path('', views.principal, name='principal'),#sempre será o ultimo pq ele tem a permissão maior que as demais

]
