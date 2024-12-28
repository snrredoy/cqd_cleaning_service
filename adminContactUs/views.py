from django.shortcuts import render , redirect
from .models import ContactUs
from .forms import ContactUsForm
from django.contrib import messages
from adminControl.models import General
from adminControl.forms import GeneralForm
import uuid
from uuid import UUID

# Create your views here.

def showContactUs(request):
    form = GeneralForm(instance=General.objects.first())
    contactUs = ContactUs.objects.all()

    context = {
        'form': form,
        'contactUs': contactUs,
        'title': 'Contact Us',
        'breadcrumb': 'Contact Us',
    }

    return render(request, 'adminControl/contactUs/showContactUs.html', context=context)

def updateContactUs(request , pk):
    instance = ContactUs.objects.get(pk=pk)
    if request.method == 'POST':
        contactUsForm = ContactUsForm(request.POST , request.FILES , instance=instance)
        if contactUsForm.is_valid():
            contactUsForm.save()
            messages.success(request, 'Contact Us Updated Successfully')
            return redirect('showContactUs')
        else:
            messages.error(request, 'Please check the form again.')
            return redirect('updateContactUs' , pk=pk)
    else:
        contactUsForm = ContactUsForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'contactUsForm': contactUsForm,
        'title': 'Update Contact Us',
        'breadcrumb': 'Contact Us',
    }

    return render(request, 'adminControl/contactUs/updateContactUs.html', context=context)

