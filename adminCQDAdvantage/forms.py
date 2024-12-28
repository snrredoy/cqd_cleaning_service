from django import forms
from .models import CQDAdvantage , CQDAdvantageSection
from adminControl.models import General
from ckeditor.widgets import CKEditorWidget

class CQDAdvantageSectionForm(forms.ModelForm):
    class Meta:
        model = CQDAdvantageSection
        fields = '__all__'
        widgets = {
            'title': CKEditorWidget(),
            'subtitle': CKEditorWidget(),
        }

class CQDAdvantageForm(forms.ModelForm):
    class Meta:
        model = CQDAdvantage
        fields = '__all__'
        widgets = {
            'title': CKEditorWidget(),
            'description': CKEditorWidget(),
        }