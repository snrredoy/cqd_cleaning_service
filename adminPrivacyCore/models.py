from django.db import models


# Create your models here.
class PrivacyCoreImage(models.Model):
    image = models.ImageField(upload_to='privacyCore/' , null=True, blank=True)

    def __str__(self):
        return f"Privacy Core Image {self.id}"
    
class PrivacyCore(models.Model):
    icon = models.ImageField(upload_to='privacyCoreIcon/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title