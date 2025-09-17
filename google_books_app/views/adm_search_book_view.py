from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SearchBookByTitle(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        if not title:
            Response(
                {"error": "Informe um Titulo para buscar detalhes sobre ele!"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        