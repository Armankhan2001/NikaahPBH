from django import forms
from .models import Profile
print("form")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'location', 'profession', 'image']
