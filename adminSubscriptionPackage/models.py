from django.db import models

# Create your models here.

class SubscriptionPackage(models.Model):
    packageIcon = models.ImageField(upload_to='subscriptionPackageIcon/')
    packageName = models.CharField(max_length=100)
    packagePrice = models.CharField(max_length=100)
    minimumClient = models.CharField(max_length=100)

    def __str__(self):
        return self.packageName
