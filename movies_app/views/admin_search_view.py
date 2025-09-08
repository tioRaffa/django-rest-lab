import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from movies_app.api.search_name import search_movie_by_name


class SearchMovieByNameAdminAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request):
        title = request.query_params.get('titulo')
        if not title:
            return Response({
                'error': 'Informe o parametro TITULO.'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        movies_data = search_movie_by_name(title)
        if movies_data:
            return Response(
                movies_data, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Nenhum filme encontrado com o título informado."},
                status=status.HTTP_404_NOT_FOUND
            )
            
            