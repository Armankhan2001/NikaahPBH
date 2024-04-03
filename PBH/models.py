

from django.db import models

class Profile(models.Model):
    id = models.AutoField(primary_key=True)  # Add id field
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images',null=True, blank=True)

    def __str__(self):
        return self.name

