from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from apps.custom_auth.forms import RegisterForm

class AuthView:
    def login_view(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "message": "Invalid credentials"})
        return render(request, "auth/login.html")

    def register_view(request):
        last_message = None
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                last_message = "Registrasi berhasil! Silakan login."
                messages.success(request, last_message)
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form, 'title': 'Register', 'last_message': last_message})
    
    def logout_view(request):
        logout(request)
        return redirect("login")
