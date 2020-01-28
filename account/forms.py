from django import forms
from .models import *
class UserAccount(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields=["Name","username","Mobile","Password"]