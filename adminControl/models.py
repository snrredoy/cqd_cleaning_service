from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class General(models.Model):
    favicon = models.ImageField(upload_to='favicon/', default="")
    navLogo = models.ImageField(upload_to='logo/', default="")
    banner = models.ImageField(upload_to='banner/', default="")
    title = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=15, null=True, blank=True)
    buttonText = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    state= models.CharField(max_length=100, default="")
    zipCode= models.IntegerField(MaxLengthValidator(6, "Zip code must be 6 digits long."), default=0)
    city= models.CharField(max_length=100, default="")


class TrustedPartner(models.Model):
    partner_one = models.ImageField(upload_to='partner/', default="")


class CommercialServices(models.Model):
    icon = models.ImageField(upload_to='icon/', default="")
    wattermarkIcon = models.ImageField(upload_to='wattermarkIcon/', default="")
    serviceTitle = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")
    mainTitle = models.CharField(max_length=100, default="")


class InteractivePlatform(models.Model):
    image = models.ImageField(upload_to='platform/', default="")

    def __str__(self):
        return f"Interactive Platform {self.id}"

    
class InteractivePlatformList(models.Model):
    icon = models.ImageField(upload_to='icon/', default="")
    title = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=100, default="")

    interactivePlatform = models.ForeignKey(InteractivePlatform, on_delete=models.CASCADE , related_name='InteractivePlatformList')

    def __str__(self):
        return self.title


class WhySubscriptionShare(models.Model):
    title = models.CharField(max_length=100, default="")
    subTitle = models.CharField(max_length=100, default="")


    def __str__(self):
        return self.title
    
class WhySubscriptionShareList(models.Model):
    icon = models.ImageField(upload_to='subscriptionIcon/', default="")
    modelTitle = models.CharField(max_length=100,default="")
    modelDescription = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.modelTitle
    