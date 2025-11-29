from django.urls import path
from . import views

# URL patterns for our movie app - pretty basic CRUD setup
urlpatterns = [
    path('', views.home, name='home'),  # landing page
    path('movies/', views.movie_list, name='movie_list'),  # all movies
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),  # single movie view
    path('search/', views.movie_search, name='movie_search'),  # search functionality
    path('movie/add/', views.movie_add, name='movie_add'),  # create new movie
    path('movie/<int:id>/edit/', views.movie_edit, name='movie_edit'),  # edit existing
    path('movie/<int:id>/delete/', views.movie_delete, name='movie_delete'),  # delete movie
    path('register/', views.register, name='register'),  # user registration
    path('logout/', views.custom_logout, name='logout'),  # custom logout view
    # TODO: might add movie ratings or comments later
]