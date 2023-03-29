from django import forms 

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

