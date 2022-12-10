from django import forms
from .models import Member2
class MemberForm(forms.ModelForm):
    
    class Meta:
        model = Member2
        fields = ['name', 'email', 'subject', 'message']
