import uuid
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='contactUsImage/')
    title = RichTextField()
    description = RichTextField()
    buttonText = models.CharField(max_length=50, default='Contact Us Now')

    def __str__(self):
        return self.title