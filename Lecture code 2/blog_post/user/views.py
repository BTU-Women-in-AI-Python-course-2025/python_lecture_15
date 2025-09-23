from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from user.forms import UserRegistrationForm
from user.models import CustomUser

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('class_blog_list')
