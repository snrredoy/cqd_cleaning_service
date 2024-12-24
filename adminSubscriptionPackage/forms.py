from .models import SubscriptionPackage
from django import forms

class SubscriptionPackageForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPackage
        fields = '__all__'