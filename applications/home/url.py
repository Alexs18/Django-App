from django.urls import path

from . import views
# from applications.home.url
# esta es la forma en que se pasan los urls como si se pasara
# en express o en angular

urlpatterns = [
    path('home/', views.Home.as_view()),
    path('home/formulario', views.Formulario.as_view()),
    path('home/ListaProductos', views.ListaProductos.as_view())
]