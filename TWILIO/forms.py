from django import forms
from .models import *

class CodeForm(forms.ModelForm):
    Number_Code = forms.CharField(label='Code', help_text='Enter sms verification code')
    class Meta: 
        model = CODE 
        fields = ('Number_Code',) 

        