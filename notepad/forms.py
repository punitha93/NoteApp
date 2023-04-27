from django import forms
from django.contrib.auth.models import User
from notepad.models import Notes

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
          
class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
