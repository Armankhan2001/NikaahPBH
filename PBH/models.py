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


    # New Fields
    introduction = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    gmail_id = models.EmailField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(upload_to='profile_images', null=True, blank=True)
    image2 = models.ImageField(upload_to='profile_images', null=True, blank=True)
    image3 = models.ImageField(upload_to='profile_images', null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    native_place = models.CharField(max_length=100, null=True, blank=True)
    current_living_in = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    mother_occupation = models.CharField(max_length=100, null=True, blank=True)
    father_occupation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name




















    