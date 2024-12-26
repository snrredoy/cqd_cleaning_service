from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class CleaningServiceHeadding(models.Model):
    title = RichTextField()
    # content = RichTextUploadingField()

    def __str__(self):
        return self.title
    
class CleaningService(models.Model):
    icon = models.ImageField(upload_to='cleaningServiceIcon/')
    watermarkIcon = models.ImageField(upload_to='cleaningServiceWatermarkIcon/')
    title = RichTextField()
    description = RichTextField()

    def __str__(self):
        return self.title