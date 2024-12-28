from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class General(models.Model):
    favicon = models.ImageField(upload_to='favicon/' )
    navLogo = models.ImageField(upload_to='logo/' )
    banner = models.ImageField(upload_to='banner/' )
    title = models.CharField(max_length=100 )
    contact = models.CharField(max_length=15)
    buttonText = models.CharField(max_length=100 )
    address = models.CharField(max_length=100 )
    state= models.CharField(max_length=100 )
    zipCode= models.IntegerField(MaxLengthValidator(6, "Zip code must be 6 digits long."))
    city= models.CharField(max_length=100 )


class TrustedPartner(models.Model):
    partner_one = models.ImageField(upload_to='partner/' )


class CommercialServices(models.Model):
    icon = models.ImageField(upload_to='icon/' )
    wattermarkIcon = models.ImageField(upload_to='wattermarkIcon/' )
    serviceTitle = models.CharField(max_length=100 )
    description = models.CharField(max_length=100 )
    mainTitle = models.CharField(max_length=100 )


class InteractivePlatform(models.Model):
    image = models.ImageField(upload_to='platform/' )

    def __str__(self):
        return f"Interactive Platform {self.id}"

    
class InteractivePlatformList(models.Model):
    icon = models.ImageField(upload_to='icon/' )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100 )

    interactivePlatform = models.ForeignKey(InteractivePlatform, on_delete=models.CASCADE , related_name='InteractivePlatformList')

    def __str__(self):
        return self.title


class WhySubscriptionShare(models.Model):
    title = models.CharField(max_length=100 )
    subTitle = models.CharField(max_length=100 )


    def __str__(self):
        return self.title
    
class WhySubscriptionShareList(models.Model):
    icon = models.ImageField(upload_to='subscriptionIcon/' )
    modelTitle = models.CharField(max_length=100)
    modelDescription = models.CharField(max_length=100 )

    def __str__(self):
        return self.modelTitle
    