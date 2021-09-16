
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('crear/', UserCreateView.as_view(), name='user_create'),
    path('change-password/', PasswordChangeView.as_view(template_name='account/change-password.html'),),

]