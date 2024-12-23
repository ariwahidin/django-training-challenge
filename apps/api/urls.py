from django.urls import path
from .views import ApiBookView, BookView

urlpatterns = [
    path('book/', ApiBookView.as_view(), name='api_book'),
    path('book/<uuid:pk>', ApiBookView.as_view(), name='api_book'),
    path('books/', BookView.get_books, name='api_book'),
    path('books/<uuid:pk>', BookView.get_books, name='api_book'),
]