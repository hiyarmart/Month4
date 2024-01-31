from rest_framework import serializers
from .models import Director, Movie, Review

def validate_name_length(value, min_length):
    if len(value) < min_length:
        raise serializers.ValidationError(f'минимальное количество букв {min_length}')

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movie_count(self, obj):
        return obj.movies.count()

    def validate_name(self, value):
        validate_name_length(value, 3)
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        validate_name_length(value, 3)
        return value

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    def validate_name(self, value):
        validate_name_length(value, 3)
        return value




