from django import forms
from .models import ContactUs
from ckeditor.widgets import CKEditorWidget

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'title': CKEditorWidget(),
            'description': CKEditorWidget(),
        }