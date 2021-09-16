from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django .contrib.auth.forms import UserCreationForm

from .forms import UserForm


class UserCreateView(CreateView):
    model = User
    template_name = 'account/user_create.html'
    form_class = UserForm
    success_url = reverse_lazy('login')


