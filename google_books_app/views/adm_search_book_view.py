from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google_books_app.service.search_book import search_by_title


class SearchBookByTitle(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        if not title:
            Response(
                {"error": "Informe um Titulo para buscar detalhes sobre ele!"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        book_data = search_by_title(title=title)
        return Response(book_data, status=status.HTTP_200_OK)
            
        