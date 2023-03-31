from django import forms
from .models import ERRORCASE


class ErrorForm(forms.ModelForm):
   

    class Meta:
         model = ERRORCASE
         fields=('error_01','error_02','error_03',)