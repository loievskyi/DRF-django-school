from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import (
    MovieListSerialiser, MovieDetailSerialiser, ReviewCreateSerializer
)


class MovieListView(APIView):
    """Displaying a list of movies"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerialiser(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class MovieDetailView(APIView):
    """Displaying the details of the movie"""
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerialiser(movie)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Adding a review to the movie"""
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid(raise_exception=True):
            review.save()
            return Response(status=201, data=review.data)
