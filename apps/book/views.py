from django.shortcuts import render

from apps.api.serializers import BookSerializer
from .forms import BookForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# @login_required
class BookView():
    @login_required
    def book_create(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Book added successfully")
                return redirect('book_list')
        else:
            form = BookForm()
        return render(request, 'book/book_form.html', {'form': form, 'title': 'Add New Book'})
    @login_required
    def book_list(request):
        books = Book.objects.all()
        return render(request, 'book/book_list.html', {'books': books})
    
    @login_required
    def book_update(request, pk):
        book = get_object_or_404(Book, uuid=pk)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request, "Book updated successfully")
                return redirect('book_list')
        else:
            form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {'form': form, 'title': 'Edit Book'}) 
    
    def book_layout(request):
        return render(request, 'layout/example_layout.html')

