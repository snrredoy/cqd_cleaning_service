from django.db import models


# Create your models here.
class PrivacyCoreImage(models.Model):
    image = models.ImageField(upload_to='privacyCore/' , default="")

    def __str__(self):
        return f"Privacy Core Image {self.id}"
    
class PrivacyCore(models.Model):
    icon = models.ImageField(upload_to='privacyCoreIcon/',default="")
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title