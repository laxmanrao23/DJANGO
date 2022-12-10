from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['First_Name', 'Last_Name', 'DOB',
                  'dropdown', 'email', 'password', 'phone']
