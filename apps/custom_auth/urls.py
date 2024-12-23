from django.urls import path
from .views import AuthView

urlpatterns = [
    path('register/', AuthView.register_view, name='register'),
    path('login/', AuthView.login_view, name='login'),
    path('logout/', AuthView.logout_view, name='logout'),
]