from django.contrib import messages
from django.shortcuts import redirect, render , get_object_or_404
from .models import General , TrustedPartner , CommercialServices , InteractivePlatform , InteractivePlatformList , WhySubscriptionShare , WhySubscriptionShareList 
from .forms import GeneralForm , TrustedPartnerForm , CommercialServicesForm , InteractivePlatformForm , InteractivePlatformListForm , WhySubscriptionShareForm , WhySubscriptionShareListForm  


# Create your views here.
def dashboard(request):
    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/dashboard/dashboard.html' , {'form': form , 'title': '' , 'breadcrumb': 'DashBoard'})


def updateGeneralSetting(request , pk):

    instance = get_object_or_404(General, pk=pk)
    if request.method == 'POST':
        form = GeneralForm(request.POST, request.FILES , instance= instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successful')
            return redirect('updateGeneralSetting', pk =10)
        else:
            messages.error(request, 'Update Failed , Please Check the form again')
            return redirect('updateGeneralSetting', pk =10)
    else:
        form = GeneralForm(instance=instance)

    return render(request, 'adminControl/generalSetting/update.html' , {'form': form , 'title': 'Update General Info' , 'breadcrumb': 'General Info'})



def addTrustedPartner(request):
    if request.method == 'POST':

        partner_count = TrustedPartner.objects.count()

        if partner_count >= 8:
            messages.error(request, "You cannot upload more than 8 Trusted Partners.")
            return redirect('showTrustedPartners')

        trustedForm = TrustedPartnerForm(request.POST , request.FILES)
        if trustedForm.is_valid():
            trustedForm.save()
            messages.success(request, 'Partner Added Successfully')
            return redirect('showTrustedPartners')
        else:
            messages.error(request, 'Partner Adding Failed , Please Check the form again')
            return redirect('addTrustedPartner')
    else:
        trustedForm = TrustedPartnerForm()

    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/trustedPartner/create.html' , {'form': form , 'trustedForm': trustedForm , 'title': 'Add Partner' , 'breadcrumb': 'Trusted Partner'})

def showTrustedPartners(request):
    form = GeneralForm(instance=General.objects.first())
    trustedPartners  = TrustedPartner.objects.all()

    return render(request, 'adminControl/trustedPartner/showPartners.html' , {'form': form , 'trustedPartners': trustedPartners , 'title': 'Partner List' , 'breadcrumb': 'Trusted Partner'})

def updateTrustedPartner(request , pk):
    instance = get_object_or_404(TrustedPartner, pk=pk)
    if request.method == 'POST':
        trustedForm = TrustedPartnerForm(request.POST , request.FILES , instance= instance)
        if trustedForm.is_valid():
            trustedForm.save()
            messages.success(request, 'Partner Update Successful')
            return redirect('showTrustedPartners')
        else:
            messages.error(request, 'Partner Update Failed , Please Check the form again')
            return redirect('updateTrustedPartner', pk=pk)
    else:
        trustedForm = TrustedPartnerForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/trustedPartner/update.html' , {'form': form , 'trustedForm': trustedForm , 'title': 'Update Partner' , 'breadcrumb': 'Trusted Partner'})

def deleteTrustedPartner(request , pk):
    instance = get_object_or_404(TrustedPartner, pk=pk)
    instance.delete()
    messages.success(request, 'Partner Deleted Successfully')
    return redirect('showTrustedPartners')




def addCommercialServices(request):
    if request.method == 'POST':
        commercialServicesForm = CommercialServicesForm(request.POST , request.FILES)
        if commercialServicesForm.is_valid():
            commercialServicesForm.save()
            messages.success(request, 'Service Added Successfully')
            return redirect('showCommercialServices')
        else:
            messages.error(request, 'Service Adding Failed , Please Check the form again')
            return redirect('addCommercialServices')
    else:
        commercialServicesForm = CommercialServicesForm()

    form = GeneralForm(instance=General.objects.first())

    return render(request, 'adminControl/commercialServices/create.html' , {'form': form , 'commercialServicesForm': commercialServicesForm , 'title': 'Add Commercial Service' , 'breadcrumb': 'Commercial Service'})


def showCommercialServices(request):
    form = GeneralForm(instance=General.objects.first())
    commercialServices  = CommercialServices.objects.all()

    return render(request, 'adminControl/commercialServices/showServices.html' , {'form': form , 'commercialServices': commercialServices , 'title': 'Commercial Services' , 'breadcrumb': 'Commercial Service'})



def updateCommercialServices(request , pk):
    instance = CommercialServices.objects.get(pk=pk)
    if request.method == 'POST':
        commercialServicesForm = CommercialServicesForm(request.POST , request.FILES , instance= instance)
        if commercialServicesForm.is_valid():
            commercialServicesForm.save()
            messages.success(request, 'Service Update Successful')
            return redirect('showCommercialServices')
        else:
            messages.error(request, 'Service Update Failed , Please Check the form again')
            return redirect('updateCommercialServices', pk=pk)
    else:
        commercialServicesForm = CommercialServicesForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'commercialServicesForm': commercialServicesForm,
        'title': 'Update Commercial Service',
        'breadcrumb': 'Commercial Service'
    }

    return render(request, 'adminControl/commercialServices/update.html' , context = context )


def deleteCommercialServices(request , pk):
    instance = get_object_or_404(CommercialServices, pk=pk)
    instance.delete()
    messages.success(request, 'Service Deleted Successfully')
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
        'breadcrumb': 'Interactive Platform'
    }

    return render(request, 'adminControl/interactivePlatform/showInteractivePlatform.html' , context = context)


def updateInteractivePlatformList(request, pk):
    instance = InteractivePlatformList.objects.get( pk=pk )
    platformInstance = InteractivePlatform.objects.get( pk=1 )
    if request.method == 'POST':
        interactivePlatformListForm = InteractivePlatformListForm(request.POST, request.FILES, instance=instance)
        interactivePlatformForm = InteractivePlatformForm(request.POST, request.FILES, instance=platformInstance)
        if interactivePlatformListForm.is_valid() and interactivePlatformForm.is_valid():
            interactivePlatformListForm.save()
            interactivePlatformForm.save()
            messages.success(request, 'Interactive Platform Update Successful')
            return redirect('showInteractivePlatform')
        else:
            messages.error(request, 'Interactive Platform Update Failed , Please Check the form again')
            return redirect('updateInteractivePlatformList', pk=pk)
    else:
        interactivePlatformListForm = InteractivePlatformListForm(instance=instance)
        interactivePlatformForm = InteractivePlatformForm(instance=platformInstance)

    form = GeneralForm(instance=General.objects.first())

    interactivePlatforms = InteractivePlatform.objects.all()

    context = {
        'form': form,
        'interactivePlatformListForm': interactivePlatformListForm,
        'interactivePlatformForm': interactivePlatformForm,
        'interactivePlatforms': interactivePlatforms,
        'title': 'Update Interactive Platform',
        'breadcrumb': 'Interactive Platform'
    }

    return render(request, 'adminControl/interactivePlatform/update.html', context=context)


def updateWhySubscriptionShare(request , pk):
    instance = WhySubscriptionShare.objects.get( pk=pk )
    if request.method == 'POST':
        whySubscriptionShareForm = WhySubscriptionShareForm(request.POST, request.FILES, instance=instance)
        if whySubscriptionShareForm.is_valid():
            whySubscriptionShareForm.save()
            messages.success(request, 'Subscription Share Title Update Successful')
            return redirect('showWhySubscriptionShareList')
        else:
            messages.error(request, 'Subscription Share Update Failed , Please Check the form again')
            return redirect('updateWhySubscriptionShare' , pk=pk)

    else:
        whySubscriptionShareForm = WhySubscriptionShareForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())
    context = {
        'form': form,
        'whySubscriptionShareForm': whySubscriptionShareForm,
        'alert' : "Update Successful",
        'title': 'Update Why Subscription Share',
        'breadcrumb': 'Subscription Share'
    }

    return render(request, 'adminControl/subscriptionShare/whySubscriptionShare/update.html', context=context)


def showWhySubscriptionShareList(request):
    form = GeneralForm(instance=General.objects.first())
    whySubscriptionShare = WhySubscriptionShare.objects.first()
    whySubscriptionShareList = WhySubscriptionShareList.objects.all()

    context = {
        'form': form,
        'whySubscriptionShare': whySubscriptionShare,
        'whySubscriptionShareLists': whySubscriptionShareList,
        'title': 'Subscription Share List',
        'breadcrumb': 'Subscription Share'
    }

    return render(request ,'adminControl\subscriptionShare\whySubscriptionShareList\showSubscriptionShareList.html', context=context)

def updateWhySubscriptionShareList(request , pk):
    instance = WhySubscriptionShareList.objects.get( pk=pk )
    if request.method == 'POST':
        whySubscriptionShareListForm = WhySubscriptionShareListForm(request.POST, request.FILES, instance=instance)
        if whySubscriptionShareListForm.is_valid():
            whySubscriptionShareListForm.save()
            messages.success(request, 'Subscription Share List Update Successful')
            return redirect('showWhySubscriptionShareList')
        else:
            messages.error(request, 'Subscription Share List Update Failed , Please Check the form again')
            return redirect('updateWhySubscriptionShareList' , pk=pk)
    else:
        whySubscriptionShareListForm = WhySubscriptionShareListForm(instance=instance)    

    form = GeneralForm(instance=General.objects.first())
    context = {
        'form': form,
        'whySubscriptionShareListForm': whySubscriptionShareListForm,
        'title': 'Update Subscription Share List',
        'breadcrumb': 'Subscription Share'
    }

    return render(request, 'adminControl/subscriptionShare/whySubscriptionShareList/update.html', context=context)
