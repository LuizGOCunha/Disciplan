from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_c = forms.CharField(
        label="Confirm your password", max_length=50, widget=forms.PasswordInput
    )


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class ActivitiesForm(forms.Form):
    DIFFICULTY_CHOICES = (
        (100, "very easy (100 pts)"),
        (200, "easy (200 pts)"),
        (300, "medium (300 pts)"),
        (400, "hard (400 pts)"),
        (500, "very hard (500 pts)"),
    )
    title = forms.CharField(max_length=100)
    description = forms.CharField(required=False, widget=forms.Textarea)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
