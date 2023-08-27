from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserRegister(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')
