from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'same password'}
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
        }


class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}),
        }