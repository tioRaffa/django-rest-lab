from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from google_books_app.models.book_model import BookModel
from google_books_app.serializer.book_serializer import BookSerializer
from django.db.models import Q
from google_books_app.service.fetch_book import fetch_by_id
from google_books_app.service.format_book_data import format_book_data

class ListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        elif self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
    
    def get(self, request):
        books = BookModel.objects.all()
        filters = Q()
        
        filter_title = request.query_params.get('title')
        if filter_title:
            filters &= Q(title__icontains=filter_title)
        
        filter_category = request.query_params.get('category')
        if filter_category:
            filters &= Q(categories__id__in=filter_category)
            
        filter_author = request.query_params.get('author')
        if filter_author:
            filters &= Q(authors__id__in=filter_author)
            
        books = books.filter(filters).distinct()
        
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
        