from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import SubscriptionPackage
from adminControl.models import General
from .forms import SubscriptionPackageForm
from adminControl.forms import GeneralForm

# Create your views here.
def addSubscriptionPackage(request):
    if request.method == 'POST':
        subscriptionPackageForm = SubscriptionPackageForm(request.POST , request.FILES)
        if subscriptionPackageForm.is_valid():
            subscriptionPackageForm.save()
            messages.success(request, 'Subscription Package added successfully.')
            return redirect('showSubscriptionPackage')
        else:
            messages.error(request, 'Failed to add Subscription Package.')
            return redirect('addSubscriptionPackage')
    else:
        subscriptionPackageForm = SubscriptionPackageForm()

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'subscriptionPackageForm': subscriptionPackageForm,
        'title': 'Add Subscription Package',
        'breadcrumb': 'Subscription Package',
    }

    return render(request, 'adminControl/subscriptionPackage/create.html', context=context)


def showSubscriptionPackage(request):
    form = GeneralForm(instance=General.objects.first())
    subscriptionPackages = SubscriptionPackage.objects.all()

    context = {
        'form': form,
        'subscriptionPackages': subscriptionPackages,
        'title': 'Subscription Package',
        'breadcrumb': 'Subscription Package',
    }

    return render(request, 'adminControl/subscriptionPackage/showSubscriptionPackages.html', context=context)


def updateSubscriptionPackage(request, pk):
    instance = SubscriptionPackage.objects.get(pk=pk)
    if request.method == 'POST':
        subscriptionPackageForm = SubscriptionPackageForm(request.POST, request.FILES, instance=instance)
        if subscriptionPackageForm.is_valid():
            subscriptionPackageForm.save()
            messages.success(request, 'Subscription Package updated successfully.')
            return redirect('showSubscriptionPackage')
        else:
            messages.error(request, 'Failed to update Subscription Package.')
            return redirect('showSubscriptionPackage')
    else:
        subscriptionPackageForm = SubscriptionPackageForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'subscriptionPackageForm': subscriptionPackageForm,
        'title': 'Update Subscription Package',
        'breadcrumb': 'Subscription Package',
    }

    return render(request, 'adminControl/subscriptionPackage/update.html', context=context)

def deleteSubscriptionPackage(request, pk):
    subscriptionPackage = SubscriptionPackage.objects.get(pk=pk)
    subscriptionPackage.delete()
    messages.success(request, 'Subscription Package deleted successfully.')
    return redirect('showSubscriptionPackage')