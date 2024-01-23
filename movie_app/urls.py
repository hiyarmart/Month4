from django.urls import path

from movie_app import views

urlpatterns = [
    path('directors/', views.director_list),
    path('directors/<int:id>/', views.director_detail),
    path('movies/', views.movie_list),
    path('movies/<int:id>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:id>/', views.review_detail),
]
