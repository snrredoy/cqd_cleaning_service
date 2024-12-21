from django.shortcuts import render
from adminControl.models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList

# Create your views here.
def home(request):
    generalData = General.objects.all().first()
    trustedPartners = TrustedPartner.objects.all()
    commercialServices = CommercialServices.objects.all()
    interactivePlatform = InteractivePlatform.objects.first()
    interactivePlatformList = InteractivePlatformList.objects.all()

    context = {
        'generalData': generalData,
        'trustedPartners': trustedPartners,
        'commercialServices': commercialServices,
        'interactivePlatforms': interactivePlatform,
        'interactivePlatformLists': interactivePlatformList
    }
    return render(request, 'base.html' , context=context)
