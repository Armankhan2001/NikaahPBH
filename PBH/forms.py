from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'location', 'profession', 'image','contact_number','instagram_id','gender']

class ProfileFormDesc(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['introduction', 'message', 'gmail_id', 'image1', 'image2','image3','dob','education','native_place','current_living_in','religion','mother_occupation','father_occupation']

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        if not str(contact_number).isdigit():
            raise forms.ValidationError("Contact number must contain only digits.")
        return contact_number



