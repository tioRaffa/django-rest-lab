from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google_books_app.models.book_model import BookModel
from google_books_app.serializer.book_serializer import BookSerializer

from google_books_app.service.fetch_book import fetch_by_id
from google_books_app.service.format_book_data import format_book_data

class ListCreateAPIView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        google_book_id = request.data.get('google_book_id')
        if not google_book_id:
            return Response(
                {"error": "Informe um ID valido em: google_book_id"}, status=status.HTTP_400_BAD_REQUEST
            )
            
        if BookModel.objects.filter(google_book_id=google_book_id).exists():
            return Response(
                {"error": "Este livro já foi cadastrado no banco de dados."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            api_data = fetch_by_id(google_book_id)
            formated_data = format_book_data(api_data)
            
            serializer = BookSerializer(data=formated_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
        except ValueError as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                    {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
                )
        