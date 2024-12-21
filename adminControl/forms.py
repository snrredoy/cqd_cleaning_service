from .models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList
from django import forms

class GeneralForm(forms.ModelForm):
    class Meta:
        model = General
        fields = '__all__'


class TrustedPartnerForm(forms.ModelForm):
    class Meta:
        model = TrustedPartner
        fields = '__all__'


class CommercialServicesForm(forms.ModelForm):
    class Meta:
        model = CommercialServices
        fields = '__all__'


class InteractivePlatformForm(forms.ModelForm):
    class Meta:
        model = InteractivePlatform
        fields = '__all__'


class InteractivePlatformListForm(forms.ModelForm):
    class Meta:
        model = InteractivePlatformList
        fields = '__all__'