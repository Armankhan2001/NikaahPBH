from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

def default_profile_image():
        return 'default_image/default_profile_image.png'  # Default image for unspecified gender




class Profile(models.Model):
    id = models.AutoField(primary_key=True)  # Add id field
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=13, null=False, unique=True, validators=[
        MinLengthValidator(10, message="Contact number must be at least 10 digits."),
        MaxLengthValidator(13, message="Contact number must be at most 13 digits.")
    ])
    instagram_id = models.CharField(max_length=100, null=True)  # Add Instagram ID field
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True)  # Add gender field
    image = models.ImageField(upload_to='profile_images', null=True, blank=True, default=default_profile_image)

    def __str__(self):
        return self.name




















    