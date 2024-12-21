from django.db import models

# Create your models here.
class General(models.Model):
    favicon = models.ImageField(upload_to='favicon/', null=True, blank=True)
    navLogo = models.ImageField(upload_to='logo/', null=True, blank=True)
    banner = models.ImageField(upload_to='banner/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    buttonText = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    state= models.CharField(max_length=100, null=True, blank=True)
    zipCode= models.CharField(max_length=100, null=True, blank=True)
    city= models.CharField(max_length=100, null=True, blank=True)


class TrustedPartner(models.Model):
    partner_one = models.ImageField(upload_to='partner/', null=True, blank=True)


class CommercialServices(models.Model):
    icon = models.ImageField(upload_to='icon/', null=True, blank=True)
    wattermarkIcon = models.ImageField(upload_to='wattermarkIcon/', null=True, blank=True)
    serviceTitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    mainTitle = models.CharField(max_length=100, null=True, blank=True)


class InteractivePlatform(models.Model):
    image = models.ImageField(upload_to='platform/', null=True, blank=True)

    def __str__(self):
        return f"Interactive Platform {self.id}"

    
class InteractivePlatformList(models.Model):
    icon = models.ImageField(upload_to='icon/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    interactivePlatform = models.ForeignKey(InteractivePlatform, on_delete=models.CASCADE , related_name='InteractivePlatformList')

    def __str__(self):
        return self.title


