from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('peliculas/', views.listado_peliculas, name='peliculas'),  # Ruta para el listado de películas
    path('peliculas/agregar/', views.agregar_editar_pelicula, name='agregar_pelicula'),
    path('peliculas/editar/<int:pelicula_id>/', views.agregar_editar_pelicula, name='editar_pelicula'),
]