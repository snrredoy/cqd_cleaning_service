from django.shortcuts import render
from adminControl.models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList , WhySubscriptionShare , WhySubscriptionShareList

# Create your views here.
def home(request):
    generalData = General.objects.all().first()
    trustedPartners = TrustedPartner.objects.all()
    commercialServices = CommercialServices.objects.all()
    interactivePlatform = InteractivePlatform.objects.first()
    interactivePlatformList = InteractivePlatformList.objects.all()
    whySubscriptionShare = WhySubscriptionShare.objects.first()
    whySubscriptionShareList = WhySubscriptionShareList.objects.all()


    context = {
        'generalData': generalData,
        'trustedPartners': trustedPartners,
        'commercialServices': commercialServices,
        'interactivePlatforms': interactivePlatform,
        'interactivePlatformLists': interactivePlatformList,
        'whySubscriptionShares': whySubscriptionShare,
        'whySubscriptionShareLists': whySubscriptionShareList,
    }
    return render(request, 'base.html' , context=context )
