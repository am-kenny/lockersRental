from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import UserBillingAddress


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")


class BillingAddressForm(forms.ModelForm):
    country = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control form-group'})
    )
    state = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control form-group'})
    )
    city = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control form-group'})
    )
    street = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Street', 'class': 'form-control form-group'})
    )
    house_number = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'House Number', 'class': 'form-control form-group'})
    )
    zip_code = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control form-group'})
    )

    class Meta:
        model = UserBillingAddress
        fields = ("country", "state", "city", "street", "house_number", "zip_code")
