#User Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#User Login
from django.contrib.auth.forms import AuthenticationForm
#Widgets
from django.forms.widgets import PasswordInput, TextInput,FileInput
from django import forms
from . models import Profile

#User Registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}


#User Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#Create a Form to Update Users
class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ['username','email']
        exclude = ['password1','password2']

#Updating profile Picture
class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    
    class Meta:
        model = Profile
        fields= ['profile_pic']