from django.shortcuts import render
from apps.api.serializers import BookSerializer
from apps.book.models import Book
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view



class BaseModelCRUDView(APIView):
    """
    Kelas dasar untuk operasi CRUD dengan pola umum
    Dapat digunakan untuk berbagai model dengan sedikit penyesuaian
    """
    model = None  # Harus didefinisikan di kelas turunan
    serializer_class = None  # Harus didefinisikan di kelas turunan

    def get_object(self, pk):
        """
        Metode umum untuk mengambil objek atau mengembalikan 404
        """
        try:
            return self.model.objects.get(uuid=pk)
        except self.model.DoesNotExist:
            raise NotFound(f"{self.model.__name__} not found")

    def get(self, request, pk=None):
        """
        Mendukung operasi list dan detail
        """
        if pk is None:
            # List semua objek
            queryset = self.model.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            # Detail objek spesifik
            instance = self.get_object(pk)
            serializer = self.serializer_class(instance)
            return Response(serializer.data)

    def post(self, request):
        """
        Membuat objek baru
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Memperbarui objek yang ada
        """
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Update stock product
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Menghapus objek
        """
        instance = self.get_object(pk)
        instance.delete()
        return Response(
            {"message": f"{self.model.__name__} deleted successfully"}, 
            status=status.HTTP_204_NO_CONTENT
        )


class ApiBookView(BaseModelCRUDView):
    permission_classes = [AllowAny]
    model = Book
    serializer_class = BookSerializer


class BookView(APIView):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def get_books(request, pk=None):
        print(request.data)
        print(pk)
        
        if pk is None:
            # List semua objek
            queryset = Book.objects.all()
            serializer = BookSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            # Detail objek spesifik
            instance = Book.objects.get(uuid=pk)
            serializer = BookSerializer(instance)
            return Response(serializer.data)
        
        # book = Book.objects.all()
        # serializer = BookSerializer(book, many=True)
        # return Response(serializer.data)