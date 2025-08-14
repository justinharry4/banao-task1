from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("signin")
    template_name = "accounts/signup.html"


class SignInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/signin.html"


class SignOutView(LogoutView):
    next_page = "signin"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"
    login_url = "signin"
