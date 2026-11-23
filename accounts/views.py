"""
App reutilizable de autenticación.

No depende de ninguna otra app del proyecto: solo usa django.contrib.auth.
Por eso puede copiarse a otro proyecto Django sin cambios.
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render


class IngresarView(LoginView):
    template_name = "accounts/login.html"


class SalirView(LogoutView):
    pass


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "accounts/registro.html", {"form": form})
