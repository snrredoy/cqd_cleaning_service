from django.shortcuts import render
from adminControl.models import General , TrustedPartner , CommercialServices

# Create your views here.
def home(request):
    generalData = General.objects.all().first()
    trustedPartners = TrustedPartner.objects.all()
    commercialServices = CommercialServices.objects.all()
    return render(request, 'base.html' , {'generalData': generalData , 'trustedPartners': trustedPartners , 'commercialServices': commercialServices})
