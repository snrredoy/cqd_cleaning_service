from django import forms
from .models import PrivacyCore, PrivacyCoreImage

class PrivacyCoreImageForm(forms.ModelForm):
    class Meta:
        model = PrivacyCoreImage
        fields = '__all__'

class PrivacyCoreForm(forms.ModelForm):
    class Meta:
        model = PrivacyCore
        fields = '__all__'