from django.urls import path

from .views import MovieListView, MovieDetailView, ReviewCreateView


urlpatterns = [
    path("movies/", MovieListView.as_view(), name="movies_list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("reviews/", ReviewCreateView.as_view()),
]
