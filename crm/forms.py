from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Myclients
from django.forms import ModelForm
from django.forms.widgets import  PasswordInput, TextInput
from django import forms
from .models import Profile, Contact


# register or create a user

class CreateuserForm(UserCreationForm):
    
    class Meta():
        
        model = User
        fields = ['username', 'password1','password2']
        
# login a user 

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
    
# form for a new client creation

class MyclientForm(forms.ModelForm):

    class Meta():
        
        model = Myclients
        
        
        fields = '__all__'
    
    


class UpdateClientForm(forms.ModelForm):

    class Meta():
        
        model = Myclients
        
        fields =  '__all__'
    
    
   

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'adress1', 'city', 'country', 'profession']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']