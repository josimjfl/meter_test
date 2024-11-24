# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from .models import OfficeEmp, CustomUser, Standard_Meter, Office



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
        ('DGM', 'DGM'),
        ('BS', 'BS'),
        ('BA', 'BA'),
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
        ('DGM', 'DGM'),
        ('BS', 'BS'),
        ('BA', 'BA'),
        ('JE', 'JE'),
        ('LT', 'LT'),
        ('LM', 'LM'),
        ('user', 'User'),
    )

    role = forms.ChoiceField(label='User Type', choices=ROLE_CHOICES)

    updated_by = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control valid',
                'name': 'updated_by',
                'id': 'updated_by',
                'onfocus': "this.placeholder = ''",
                'onblur': "this.placeholder = 'Enter Your Address'",
                'type': 'text',
                'placeholder': 'Enter updated_by value',
                'value': "1",
                'readonly': False,
            }
        )
    )

    class Meta:
        model = CustomUser
        exclude = ['password', 'is_superuser', 'last_login', 'is_staff', 'groups', 'user_permissions']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract the request object if passed
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        if self.request:  # Set the updated_by field if request is available
            user.updated_by = self.request.user.username
        if commit:
            user.save()
        return user




class OfficeEmpForm(forms.ModelForm):
    class Meta:
        model = OfficeEmp
        fields = [
            'office', 
            'tested_by', 
            'checked_by', 
            'counter_sign_by', 
            'received_by', 
            'standered_meter'
        ]
        widgets = {
            'office': forms.Select(attrs={'class': 'form-control'}),
            'tested_by': forms.Select(attrs={'class': 'form-control'}),
            'checked_by': forms.Select(attrs={'class': 'form-control'}),
            'counter_sign_by': forms.Select(attrs={'class': 'form-control'}),
            'received_by': forms.Select(attrs={'class': 'form-control'}),
            'standered_meter': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pass `user` explicitly when initializing the form
        super().__init__(*args, **kwargs)

        if user:
            if user.role == 'IT':  # If the user is IT, show offices within their PBS
                self.fields['office'].queryset = Office.objects.filter(pbs=user.office.pbs)
                self.fields['office'].widget.attrs.pop('readonly', None)  # Remove readonly if present
                self.fields['office'].disabled = False  # Allow editing for IT users
            else:  # For other roles, restrict to the user's office and make it read-only
                self.fields['office'].queryset = Office.objects.filter(id=user.office.id)
                self.fields['office'].initial = user.office
                self.fields['office'].disabled = True  # Make office read-only for non-IT roles

            # Filter other fields based on the user's office
            self.fields['tested_by'].queryset = CustomUser.objects.filter(office__pbs=user.office.pbs)
            self.fields['checked_by'].queryset = CustomUser.objects.filter(office__pbs=user.office.pbs)
            self.fields['counter_sign_by'].queryset = CustomUser.objects.filter(office__pbs=user.office.pbs)
            self.fields['received_by'].queryset = CustomUser.objects.filter(office__pbs=user.office.pbs)
            self.fields['standered_meter'].queryset = Standard_Meter.objects.filter(office__pbs=user.office.pbs)






from django import forms
from .models import Standard_Meter, Office

class StandardMeterForm(forms.ModelForm):
    class Meta:
        model = Standard_Meter
        fields = ['office', 'std_serial', 'std_name', 'std_kh']
        widgets = {
            'office': forms.Select(attrs={'class': 'form-control'}),
            'std_serial': forms.TextInput(attrs={'class': 'form-control'}),
            'std_name': forms.TextInput(attrs={'class': 'form-control'}),
            'std_kh': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Extract user from kwargs
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            # Filter office to the current user's office and pre-fill it
            self.fields['office'].queryset = Office.objects.filter(id=user.office.id)
            self.fields['office'].initial = user.office
            # Make the office field readonly
            self.fields['office'].disabled = True  # Prevent editing

    def clean_office(self):
        # Return the pre-populated office
        return self.cleaned_data['office']


