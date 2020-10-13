from django import forms
from django.contrib.auth.models import User
from .models import Video, Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length = 100)
#     password = forms.CharField(max_length = 100)

# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length = 100)
#     password = forms.CharField(max_length = 100)
#     email = forms.CharField(max_length = 100)

# class VideoForm(forms.Form):
#     title = forms.CharField(max_length = 100)
#     description = forms.CharField(max_length = 200)
#     file = forms.FileField()

# class CommentForm(forms.Form):
#     text = forms.CharField(max_length = 300, label = 'text')
