from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class GreetGuest(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=50, required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-greetingForm"
        self.helper.form_class = "form-class"
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
        
    