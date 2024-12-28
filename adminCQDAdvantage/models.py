from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class CQDAdvantageSection(models.Model):
    title = RichTextField()
    subtitle = RichTextField()

    def __str__(self):
        return self.title
    
class CQDAdvantage(models.Model):
    icon = models.ImageField(upload_to='cqdAdvantageIcon/')
    title = RichTextField()
    description = RichTextField()

    def __str__(self):
        return self.title