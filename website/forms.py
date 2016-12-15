from django import forms
from django.contrib.auth.models import User

from website.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password',
                                                                 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username',
                                               'id': 'InputUser_reg', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter email',
                                            'id': 'InputEmail_reg', 'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The Email Id Already Exists!")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name',
                                           'id': 'InputUser_userProfile', 'class': 'form-control'}),
        }
