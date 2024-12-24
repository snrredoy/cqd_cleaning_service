from .models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList , WhySubscriptionShare , WhySubscriptionShareList , SubscriptionPackage
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


class WhySubscriptionShareForm(forms.ModelForm):
    class Meta:
        model = WhySubscriptionShare
        fields = '__all__'


class WhySubscriptionShareListForm(forms.ModelForm):
    class Meta:
        model = WhySubscriptionShareList
        fields = '__all__'


class SubscriptionPackageForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPackage
        fields = '__all__'