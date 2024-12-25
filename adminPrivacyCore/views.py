from django.shortcuts import render , redirect
from django.contrib import messages
from adminControl.models import General
from .models import PrivacyCore, PrivacyCoreImage
from adminControl.forms import GeneralForm
from .forms import PrivacyCoreForm , PrivacyCoreImageForm

# Create your views here.
def showPrivacyCore(request):
    form = GeneralForm(instance=General.objects.first())
    privacyCore = PrivacyCore.objects.all()
    privacyCoreImage = PrivacyCoreImage.objects.get(id=1)
    context = {
        "form": form,
        "privacyCores": privacyCore,
        "privacyCoreImages": privacyCoreImage,
        "title": "Privacy Core",
        "breadcrumb": "Privacy Core",
    }
    return render(request, "adminControl/privacyCore/showPrivacyCore.html", context)


def updatePrivacyCore(request , pk ):
    form = GeneralForm(instance=General.objects.first())
    privacyCore = PrivacyCore.objects.get(pk=pk)
    privacyCoreImage = PrivacyCoreImage.objects.get(id=1)
    if request.method == "POST":
        privacyCoreForm = PrivacyCoreForm(request.POST , request.FILES , instance=privacyCore)
        privacyCoreImageForm = PrivacyCoreImageForm(request.POST , request.FILES , instance=privacyCoreImage)
        if privacyCoreForm.is_valid() and privacyCoreImageForm.is_valid():
            privacyCoreForm.save()
            privacyCoreImageForm.save()
            messages.success(request, "Privacy Core Updated Successfully")
            return redirect("showPrivacyCore")
        else:
            messages.error(request, "Privacy Core Update Failed , Please Check the form again")
            return redirect("updatePrivacyCore")
    else:
        privacyCoreForm = PrivacyCoreForm(instance=privacyCore)
        privacyCoreImageForm = PrivacyCoreImageForm(instance=privacyCoreImage)

    context = {
        "form": form,
        "privacyCoreForm": privacyCoreForm,
        "privacyCoreImageForm": privacyCoreImageForm,
        "title": "Update Privacy Core",
        "breadcrumb": "Privacy Core",
    }
    return render(request, "adminControl/privacyCore/update.html", context)
