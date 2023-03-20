from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput
from .models import *


class AddSongForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album'].empty_label = "Not chosen"
        self.fields['genre'].empty_label = "Not chosen"

    class Meta:
        model = Songs
        fields = ['name', 'date', 'duration', 'album', 'genre']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Songs.objects.filter(name=name).exists():
            raise forms.ValidationError('The name must be unique.')
        elif len(name) > 100:
            raise ValidationError('The name must be less than 100 characters.')
        return name

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > date.today():
            raise forms.ValidationError('The date cannot be in the future.')
        return date

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        try:
            duration_time = datetime.strptime(duration, '%M:%S').time()
        except ValueError:
            raise forms.ValidationError('Invalid duration format, use format MM:SS')
        if duration_time <= datetime.strptime('00:00', '%M:%S').time():
            raise forms.ValidationError('Duration must be greater than 0.')
        return duration

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username', 'class': 'form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email address', 'class': 'form-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
