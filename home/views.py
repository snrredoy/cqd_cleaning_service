from django.shortcuts import render
from adminControl.models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList , WhySubscriptionShare , WhySubscriptionShareList
from adminSubscriptionPackage.models import SubscriptionPackage
from adminPrivacyCore.models import PrivacyCore, PrivacyCoreImage

# Create your views here.
def home(request):
    generalData = General.objects.all().first()
    trustedPartners = TrustedPartner.objects.all()
    commercialServices = CommercialServices.objects.all()
    interactivePlatform = InteractivePlatform.objects.first()
    interactivePlatformList = InteractivePlatformList.objects.all()
    whySubscriptionShare = WhySubscriptionShare.objects.first()
    whySubscriptionShareList = WhySubscriptionShareList.objects.all()
    subscriptionPackages = SubscriptionPackage.objects.all()
    privacyCores = PrivacyCore.objects.all()
    privacyCoreImage = PrivacyCoreImage.objects.first()


    context = {
        'generalData': generalData,
        'trustedPartners': trustedPartners,
        'commercialServices': commercialServices,
        'interactivePlatforms': interactivePlatform,
        'interactivePlatformLists': interactivePlatformList,
        'whySubscriptionShares': whySubscriptionShare,
        'whySubscriptionShareLists': whySubscriptionShareList,
        'subscriptionPackages': subscriptionPackages,
        'privacyCores': privacyCores,
        'privacyCoreImage': privacyCoreImage,
    }
    return render(request, 'base.html' , context=context )
