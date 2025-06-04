from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creches/', views.lista_creches, name='lista_creches'),
    path('matricula/<int:creche_id>/', views.matricula, name='matricula'),
]

