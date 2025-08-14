from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from .models import User

class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ImageField(label="Profile Picture")
    account_type = forms.ChoiceField(
        choices=User.ACCOUNT_TYPE_CHOICES,
        widget=forms.RadioSelect(),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "account_type",
            "first_name",
            "last_name",
            "profile_image",
            "address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = 'form-group'
        self.helper.label_class = 'form-label'
        self.helper.field_class = 'mb-3'
        
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('account_type', css_class='form-control'),
            Field('first_name', css_class='form-control'),
            Field('last_name', css_class='form-control'),
            Field('profile_image', css_class='form-control'),
            Field('address', css_class='form-control', rows="4"),
            Field('password1', css_class='form-control'),
            Field('password2', css_class='form-control'),
            Submit('submit', 'Sign Up', css_class='btn btn-primary w-100 mt-3')
        )


class CustomAuthenticationForm(AuthenticationForm):    
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = 'form-group'
        self.helper.label_class = 'form-label'
        self.helper.field_class = 'mb-3'
        
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('password', css_class='form-control'),
            Submit('submit', 'Login', css_class='btn btn-primary w-100 mt-3')
        )
