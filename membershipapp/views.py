from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from membershipapp.forms import RegisterForm, UpdateProfileForm


class UserSignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile-detail.html'


class UpdateProfileView(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'edit-profile.html'

    def get_absolute_url(self):
        return reverse('profile-detail',args=[str(self.object.id)])