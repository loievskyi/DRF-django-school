from rest_framework import serializers
# from rest_framework_recursive.fields import RecursiveField

from .models import Movie, Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Retrieving a review"""

    class Meta:
        model = Review
        fields = "__all__"


class RecursiveSerializer(serializers.Serializer):
    """Retrieving children recursively"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterReviewListSerializer(serializers.ListSerializer):
    """reviews filter, parents only"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ReviewSerializer(serializers.ModelSerializer):
    """Retrieving a view"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("id", "name", "text", "children")


class MovieListSerialiser(serializers.ModelSerializer):
    """List of films"""

    class Meta:
        model = Movie
        fields = ("id", "title", "tagline", "category")


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
