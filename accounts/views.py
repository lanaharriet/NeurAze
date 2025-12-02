from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Signup view
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # --------- BASIC VALIDATION ---------

        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return render(request, "accounts/signup.html")

        # --------- EMAIL FORMAT VALIDATION ---------
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address.")
            return render(request, "accounts/signup.html")

        # --------- PASSWORD MATCH ---------
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "accounts/signup.html")

        # --------- UNIQUE USERNAME & EMAIL ---------
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "accounts/signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, "accounts/signup.html")

        # --------- PASSWORD STRENGTH VALIDATION ---------
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, "accounts/signup.html")

        # --------- CREATE USER ---------
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )

        user.save()
        messages.success(request, "Account created successfully!")
        login(request, user)

        return redirect("hub:hub")

    return render(request, "accounts/signup.html")

# Custom logout view (GET or POST safe)
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('accounts:login')
