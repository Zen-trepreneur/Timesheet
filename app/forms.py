from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, ChoiceField, ModelChoiceField, TypedChoiceField
from .models import TimeEntryModel


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('This Email Address is already registered.')
        return email


class TimeEntryModelForm(ModelForm):

    task = forms.CharField(initial="")

    class Meta:
        model = TimeEntryModel
        fields = '__all__'
