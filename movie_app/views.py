from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer


@api_view(['GET', 'PUT'])
def director_list(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    queryset = get_object_or_404(Director, id=id)
    if request.method == 'GET':
        serializer = DirectorSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    queryset = get_object_or_404(Movie, id=id)
    if request.method == 'GET':
        serializer = MovieSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = MovieSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    queryset = get_object_or_404(Review, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)


@api_view(['GET'])
def movie_review_list(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
