from django import forms
from .models import Post,ERRORCASE

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields=('title','text',)




class ErrorForm(forms.ModelForm):
   

    class Meta:
         model = ERRORCASE
         fields=('error_01','error_02','error_03',)