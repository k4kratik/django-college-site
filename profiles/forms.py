from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="100 Char Max", required=False)
    email = forms.EmailField(required=True, help_text="enter valid email")
    comment = forms.CharField(required=True, widget=forms.Textarea, help_text="Write us Something you want to convey us. We will be happy to hear you")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
