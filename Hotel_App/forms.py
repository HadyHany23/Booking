from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']

    def save(self, commit=True):
        user = super().save(commit=False)
        # If the first user being added (ID=1), make them a regular user
        if User.objects.count() == 1:
            user.is_staff = False
        if commit:
            user.save()
        return user
