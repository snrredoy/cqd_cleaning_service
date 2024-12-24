from django.db import models

# Create your models here.

class SubscriptionPackage(models.Model):
    packageIcon = models.ImageField(upload_to='subscriptionPackageIcon/', null=True, blank=True)
    packageName = models.CharField(max_length=100, null=True, blank=True)
    packagePrice = models.CharField(max_length=100, null=True, blank=True)
    minimumClient = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.packageName
