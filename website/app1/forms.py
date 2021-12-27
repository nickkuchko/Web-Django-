from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):                       # Form which is used during contact form send email
    email = forms.EmailField(required=True, label='Enter your email')
    subject = forms.CharField(required=True, label='Type the subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Type the Message')


class LoginForm(forms.Form):                         # Form which is used during log in process
    username = forms.CharField(max_length=200, label='Enter your username')
    password = forms.CharField(max_length=200, label='Enter your password')


class NewUserForm(UserCreationForm):                 # Form which is used during registration process
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
