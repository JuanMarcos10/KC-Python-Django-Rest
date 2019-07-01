from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from django.views import View

from users.forms import LoginForm, SignUpForm


class LoginView(View):
    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'login.html', context)

    def get(self, request):  # Sólo se ejecutará cuando el método de la petición HTTP sea GET
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return self.render_template_with_form(request, form)

    def post(self, request):  # Sólo se ejecutará cuando el método de la petición HTTP sea POST
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        return self.render_template_with_form(request, form)

class LogoutView(View):
    def get(self, request):
        django_logout(request)
        return redirect('login')


class SignUpView(View):
    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'signup.html', context)

    def get(self, request):  # Sólo se ejecutará cuando el método de la petición HTTP sea GET
        if request.user.is_authenticated:
            return redirect('home')

        form = SignUpForm()
        return self.render_template_with_form(request, form)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
            )
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        return self.render_template_with_form(request, form)

