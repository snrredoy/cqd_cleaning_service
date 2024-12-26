from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import CleaningServiceHeadding , CleaningService
from adminControl.models import General
from .forms import CleaningServiceHeaddingForm , CleaningServiceForm
from adminControl.forms import GeneralForm


def showCleaningService(request):
    form = GeneralForm(instance=General.objects.first())
    cleaningServices = CleaningService.objects.all()
    cleaningServiceHeadding = CleaningServiceHeadding.objects.first()

    context = {
        'form': form,
        'cleaningServices': cleaningServices,
        'cleaningServiceHeadding': cleaningServiceHeadding,
        'title': 'Cleaning Service List',
        'breadcrumb': 'Cleaning Service',
    }

    return render(request, 'adminControl/cleaningService/showCleaningService.html', context=context)

# Create your views here.
def updateCleaningServiceHeadding(request , pk):

    instance = CleaningServiceHeadding.objects.get(pk=pk)
    if request.method == 'POST':
        sectionHeadingForm = CleaningServiceHeaddingForm(request.POST , instance=instance)
        if sectionHeadingForm.is_valid():
            sectionHeadingForm.save()
            messages.success(request, 'Cleaning Service Section Heading Updated Successfully')
            return redirect('showCleaningService')
        else:
            messages.error(request, 'Please Correct the error below.')
            return redirect('updateCleaningServiceHeadding' , pk=pk)
    else:
        sectionHeadingForm = CleaningServiceHeaddingForm(instance=instance)    

    form = GeneralForm(instance=General.objects.first())
    context = {
        'form': form,
        'sectionHeadingForm': sectionHeadingForm,
        'title': 'Update Cleaning Service Section Heading',
        'breadcrumb': 'Cleaning Service',
    }
    return render(request, 'adminControl/cleaningService/updateSectionHeading.html', context=context)