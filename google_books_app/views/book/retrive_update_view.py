from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from google_books_app.models.book_model import BookModel
from google_books_app.serializer.book_serializer import BookSerializer
from django.shortcuts import get_object_or_404



class RetriveUpdateAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(BookModel, pk=pk)
    
    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [permissions.IsAdminUser()]
        elif self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        
        
    def get(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)