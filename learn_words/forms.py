from django import forms
from learn_words.models import Account, Words
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('account_picture',)
