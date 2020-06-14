from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"First Name", 'name': 'FrstName'}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Username", 'name': 'username'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Last Name", 'name': 'LastName'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control",'placeholder':"Email", 'name': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",'placeholder':"Password", 'name': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",'placeholder':"Confirm Password", 'name': 'ConfirmPassword'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]