from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from .models import CustomUser
from .forms import RegisterForm, ProfileForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class ProfileView(UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user