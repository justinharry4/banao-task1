from django.urls import path

from .views import SignUpView, SignInView, SignOutView, DashboardView


urlpatterns = [
	path('signup/', SignUpView.as_view(), name="signup"),
	path('signin/', SignInView.as_view(), name="signin"),
	path('signout/', SignOutView.as_view(), name="signout"),
	path('', DashboardView.as_view(), name="dashboard"),
]