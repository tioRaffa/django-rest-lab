from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies_app.models.movie_model import MoviesModels
from movies_app.serializers.movie_serializer import MoviesSerializer
from django.shortcuts import get_object_or_404




class MovieRetrieveUpdateView(APIView):
    def get_object(self, pk):
        return get_object_or_404(MoviesModels, pk=pk)
        
    def get(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)