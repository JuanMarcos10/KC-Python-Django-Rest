from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import CharField


class LoginForm(forms.Form):
    usr = forms.CharField(label='Username')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only..')
    first_name: CharField = forms.CharField(max_length=30, required=False, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only..')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    password_repeat = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise ValidationError("This username already exists")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password_repeat', )
