from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'location', 'profession', 'image','contact_number','instagram_id','gender']

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        if not str(contact_number).isdigit():
            raise forms.ValidationError("Contact number must contain only digits.")
        return contact_number
