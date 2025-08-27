from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from book.models import CategoryModel, BooksModel
from book.serializer import CategorySerializer, BooksSerializer


class CategoriesAPIView(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryAPIView(APIView):
    def get_object(self, pk):
        obj = get_object_or_404(CategoryModel, pk=pk)
        return obj
    
    def get(self, request, pk):
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BooksAPIView(APIView):
    def get(self, request):
        books = BooksModel.objects.all()

        # FILTRO
        category_id = request.query_params.get('category')
        if category_id:
            books = books.filter(category_id=category_id)

        title = request.query_params.get('title')
        if title:
            books = books.filter(title__icontains=title)

        author = request.query_params.get('autor')
        if author:
            books = books.filter(author__icontains=author)
        # ----

        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(BooksModel, pk=pk)
    
    def get(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)