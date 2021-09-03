from rest_framework import serializers

from .models import Movie, Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Retrieving a review"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Retrieving a view"""

    class Meta:
        model = Review
        fields = ("name", "text", "parent")


class MovieListSerialiser(serializers.ModelSerializer):
    """List of films"""

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")


class MovieDetailSerialiser(serializers.ModelSerializer):
    """Film detail"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True,
                                             many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True,
                                          many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True,
                                          many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft", )
