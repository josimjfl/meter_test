from django import forms
from .models import Test_Data

class TestDataUpdateForm(forms.ModelForm):
    class Meta:
        model = Test_Data
        exclude = [
            'created_by', 'created_date', 'office', 
            'updated_by', 'counter_sign_by', 'checked_by', 
            'checked_date', 'counter_sign_date', 
            'received_by', 'received_date'
        ]

    def __init__(self, *args, **kwargs):
        super(TestDataUpdateForm, self).__init__(*args, **kwargs)
        
        # Make all fields optional (not required)
        for field in self.fields:
            self.fields[field].required = False
