from django import forms
from .models import CleaningServiceHeadding , CleaningService
from ckeditor.widgets import CKEditorWidget


class CleaningServiceHeaddingForm(forms.ModelForm):

    title = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = CleaningServiceHeadding
        fields = '__all__'

class CleaningServiceForm(forms.ModelForm):
    class Meta:
        model = CleaningService
        fields = '__all__'
        widgets = {
            'title': CKEditorWidget(),
            'description': CKEditorWidget(),
        }