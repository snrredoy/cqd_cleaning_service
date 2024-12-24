from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class General(models.Model):
    favicon = models.ImageField(upload_to='favicon/', null=True, blank=True)
    navLogo = models.ImageField(upload_to='logo/', null=True, blank=True)
    banner = models.ImageField(upload_to='banner/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    contact = models.IntegerField(MaxLengthValidator(15, "Contact number must be 15 digits long."), null=True, blank=True)
    buttonText = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    state= models.CharField(max_length=100, null=True, blank=True)
    zipCode= models.IntegerField(MaxLengthValidator(6, "Zip code must be 6 digits long."), null=True, blank=True)
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


class WhySubscriptionShare(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    subTitle = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.title
    
class WhySubscriptionShareList(models.Model):
    icon = models.ImageField(upload_to='subscriptionIcon/', null=True, blank=True)
    modelTitle = models.CharField(max_length=100, null=True, blank=True)
    modelDescription = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.modelTitle
    

class SubscriptionPackage(models.Model):
    packageIcon = models.ImageField(upload_to='subscriptionPackageIcon/', null=True, blank=True)
    packageName = models.CharField(max_length=100, null=True, blank=True)
    packagePrice = models.CharField(max_length=100, null=True, blank=True)
    minimumClient = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.packageName