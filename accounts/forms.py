# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


#Update by user self
class UserUpdateForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Div('field1', css_class='span6'),
            Div('field3', css_class='span6'),  
        css_class='row-fluid'), 
    )

    ROLE_CHOICES = (
        ('MT', 'MT'),
        ('MTS', 'MTS'),
        ('IT', 'IT'),
        ('AGM', 'AGM'),
        ('BS', 'BS'),
        ('JE', 'JE'),
        ('LT', 'LT'),
        ('LM', 'LM'),
        ('user', 'User'),
    )

    role = forms.ChoiceField(label='User Type', choices=ROLE_CHOICES)

    updated_by = forms.CharField(
            required = True,
            widget = forms.TextInput(
                attrs={
                    'class': 'form-control valid',
                    'name': 'address',
                    'id': 'address',
                    'onfocus': 'this.placeholder = ''',
                    'onblur': "this.placeholder = 'Enter Your Address'",
                    'id': 'address',
                    'type':'text',
                    'placeholder': 'sych as: dhaka, Bangladesh',
                    'value': 'dhaka, Bangladesh'
                }
            )
        )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'mobile', 'designation', 'role', 'office', 'training_id']
        


#Update user by admin or IT
class CustomUserForm(forms.ModelForm):
    ROLE_CHOICES = (
        ('MT', 'MT'),
        ('MTS', 'MTS'),
        ('IT', 'IT'),
        ('AGM', 'AGM'),
        ('BS', 'BS'),
        ('JE', 'JE'),
        ('LT', 'LT'),
        ('LM', 'LM'),
        ('user', 'User'),
    )

    role = forms.ChoiceField(label='User Type', choices=ROLE_CHOICES)

    updated_by = forms.CharField(
            required = True,
            widget = forms.TextInput(
                attrs={
                    'class': 'form-control valid',
                    'name': 'address',
                    'id': 'address',
                    'onfocus': 'this.placeholder = ''',
                    'onblur': "this.placeholder = 'Enter Your Address'",
                    'id': 'address',
                    'type':'text',
                    'placeholder': 'sych as: dhaka, Bangladesh',
                    'value':"1",
                    'readonly': False,
                }
            )
        )
    class Meta:
        model = CustomUser
        exclude = ['password', 'is_superuser','last_login', 'is_staff', 'groups', 'user_permissions']


        def save(self, commit=True):
            user = super(CustomUserForm, self).save(commit=False)
            user.updated_by = self.request.user.username # This is logged in user info
            if commit:
                user.save()
            return user   