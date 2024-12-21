from django.shortcuts import redirect, render , get_object_or_404
from .models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList
from .forms import GeneralForm , TrustedPartnerForm , CommercialServicesForm , InteractivePlatformForm , InteractivePlatformListForm

# Create your views here.
def dashboard(request):
    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/adminBase.html' , {'form': form , 'title': '' , 'breadcrumb': 'DashBoard'})


def updateGeneralSetting(request , pk):

    instance = get_object_or_404(General, pk=pk)
    if request.method == 'POST':
        form = GeneralForm(request.POST, request.FILES , instance= instance)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('updateGeneralSetting', pk =10)
    else:
        form = GeneralForm(instance=instance)

    return render(request, 'adminControl/generalSetting/update.html' , {'form': form , 'title': 'General' , 'breadcrumb': 'General Setting'})



def addTrustedPartner(request):
    if request.method == 'POST':

        partner_count = TrustedPartner.objects.count()

        if partner_count >= 8:
            error_message = "You cannot upload more than 8 Trusted Partners."
            return render(request, 'adminControl/trustedPartner/create.html', {'error_message': error_message})

        trustedForm = TrustedPartnerForm(request.POST , request.FILES)
        if trustedForm.is_valid():
            trustedForm.save()
            return redirect('showTrustedPartners')
    else:
        trustedForm = TrustedPartnerForm()

    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/trustedPartner/create.html' , {'form': form , 'trustedForm': trustedForm , 'title': 'Add Partner' , 'breadcrumb': 'Trusted Partner Settings'})

def showTrustedPartners(request):
    form = GeneralForm(instance=General.objects.first())
    trustedPartners  = TrustedPartner.objects.all()

    return render(request, 'adminControl/trustedPartner/showPartners.html' , {'form': form , 'trustedPartners': trustedPartners , 'title': 'Partner List' , 'breadcrumb': 'Trusted Partner Setting'})

def updateTrustedPartner(request , pk):
    instance = get_object_or_404(TrustedPartner, pk=pk)
    if request.method == 'POST':
        trustedForm = TrustedPartnerForm(request.POST , request.FILES , instance= instance)
        if trustedForm.is_valid():
            trustedForm.save()
            return redirect('showTrustedPartners')
    else:
        trustedForm = TrustedPartnerForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/trustedPartner/update.html' , {'form': form , 'trustedForm': trustedForm , 'title': 'Update Partner' , 'breadcrumb': 'Trusted Partner Settings'})

def deleteTrustedPartner(request , pk):
    instance = get_object_or_404(TrustedPartner, pk=pk)
    instance.delete()
    return redirect('showTrustedPartners')




def addCommercialServices(request):
    if request.method == 'POST':
        commercialServicesForm = CommercialServicesForm(request.POST , request.FILES)
        if commercialServicesForm.is_valid():
            commercialServicesForm.save()
            return redirect('showCommercialServices')
    else:
        commercialServicesForm = CommercialServicesForm()

    form = GeneralForm(instance=General.objects.first())
    return render(request, 'adminControl/commercialServices/create.html' , {'form': form , 'commercialServicesForm': commercialServicesForm , 'title': 'Add Commercial Service' , 'breadcrumb': 'Commercial Service Settings'})


def showCommercialServices(request):
    form = GeneralForm(instance=General.objects.first())
    commercialServices  = CommercialServices.objects.all()

    return render(request, 'adminControl/commercialServices/showServices.html' , {'form': form , 'commercialServices': commercialServices , 'title': 'Commercial Services' , 'breadcrumb': 'Commercial Service Settings'})



def updateCommercialServices(request , pk):
    instance = get_object_or_404(CommercialServices, pk=pk)
    if request.method == 'POST':
        commercialServicesForm = CommercialServicesForm(request.POST , request.FILES , instance= instance)
        if commercialServicesForm.is_valid():
            commercialServicesForm.save()
            return redirect('showCommercialServices')
    else:
        commercialServicesForm = CommercialServicesForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/commercialServices/update.html' , {'form': form , 'commercialServicesForm': commercialServicesForm , 'title': 'Update Commercial Service' , 'breadcrumb': 'Commercial Service Settings'})


def deleteCommercialServices(request , pk):
    instance = get_object_or_404(CommercialServices, pk=pk)
    instance.delete()
    return redirect('showCommercialServices')

def showInteractivePlatform(request):
    form = GeneralForm(instance=General.objects.first())
    interactivePlatform  = InteractivePlatform.objects.all()
    interactivePlatformList = InteractivePlatformList.objects.all()

    context ={
        'form': form,
        'interactivePlatforms': interactivePlatform,
        'interactivePlatformLists': interactivePlatformList,
        'title': 'Interactive Platform List',
        'breadcrumb': 'Interactive Platform Settings'
    }

    return render(request, 'adminControl/interactivePlatform/showInteractivePlatform.html' , context = context)

def updateInteractivePlatform(request, pk):
    instance = get_object_or_404(InteractivePlatformList, pk=pk)
    if request.method == 'POST':
        interactivePlatformListForm = InteractivePlatformListForm(request.POST, request.FILES, instance=instance)
        if interactivePlatformListForm.is_valid():
            interactivePlatformListForm.save()
            return redirect('showInteractivePlatform')
    else:
        interactivePlatformListForm = InteractivePlatformListForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    interactivePlatforms = InteractivePlatform.objects.all()

    context = {
        'form': form,
        'interactivePlatformListForm': interactivePlatformListForm,
        'interactivePlatforms': interactivePlatforms,
        'title': 'Update Interactive Platform',
        'breadcrumb': 'Interactive Platform Settings'
    }

    return render(request, 'adminControl/interactivePlatform/update.html', context=context)