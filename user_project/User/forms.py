from django import forms
from .models import User

# Create your models here.

# class userForm(forms.Form):
#     name = forms.CharField(max_length=200,)
#     email = forms.EmailField(max_length=200)
    
class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email']
    