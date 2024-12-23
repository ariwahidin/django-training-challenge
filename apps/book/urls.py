from django.urls import path
from .views import BookView

urlpatterns = [
    path('create/', BookView.book_create, name='book_create'),
    path('list/', BookView.book_list, name='book_list'),
    path('update/<uuid:pk>/', BookView.book_update, name='book_update'),
    path('layout/', BookView.book_layout, name='book_layout'),
]