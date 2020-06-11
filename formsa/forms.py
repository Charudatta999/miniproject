from django import forms
from django.forms import ModelForm
from .models import Entry,UserProfile,Profile
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User




#
class NewUserFrom(UserCreationForm):
    email= forms.EmailField(required=True)
    photo= forms.FileField(required=False)
    firstname = forms.CharField(max_length=15,required=False)
    lastname = forms.CharField(max_length=15,required=False)
    class Meta:
        model = User
        fields = ('username', 'email' ,'password1', 'password2','photo','firstname','lastname')
    def save(self,commit=True):
        user = super(NewUserFrom, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.photo= self.cleaned_data['photo']
        user.firstname= self.cleaned_data['firstname']
        user.lastname= self.cleaned_data['lastname']
        if commit:
            user.save()
        return user

class Entryform(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title','sub_heading','author','text','photo']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'class':'materialize-textarea','palcehoder':'feel free to type','style':'margin: 0px; width: 835px; height: 393px;'})



class PostForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title','text','photo')
        widgets={
            'title':forms.TextInput()
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']