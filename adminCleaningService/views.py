from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import CleaningServiceHeadding , CleaningService
from adminControl.models import General
from .forms import CleaningServiceHeaddingForm , CleaningServiceForm
from adminControl.forms import GeneralForm
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
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

@login_required
def addCleaningService(request):
    if request.method == 'POST':
        cleaningServiceForm = CleaningServiceForm(request.POST , request.FILES)
        if cleaningServiceForm.is_valid():
            cleaningServiceForm.save()
            messages.success(request, 'Cleaning Service Added Successfully')
            return redirect('showCleaningService')
        else:
            messages.error(request, 'Please Correct the error below.')
            return redirect('addCleaningService')
    else:
        cleaningServiceForm = CleaningServiceForm()

    form = GeneralForm(instance=General.objects.first())
    context = {
        'form': form,
        'cleaningServiceForm': cleaningServiceForm,
        'title': 'Add Cleaning Service',
        'breadcrumb': 'Cleaning Service',
    }
    return render(request, 'adminControl/cleaningService/addCleaningService.html', context=context)

@login_required
def updateCleaningService(request , pk):
    instance = CleaningService.objects.get(pk=pk)
    if request.method == 'POST':
        cleaningServiceForm = CleaningServiceForm(request.POST , request.FILES , instance=instance)
        if cleaningServiceForm.is_valid():
            cleaningServiceForm.save()
            messages.success(request, 'Cleaning Service Updated Successfully')
            return redirect('showCleaningService')
        else:
            messages.error(request, 'Please check the form again.')
            return redirect('updateCleaningService' , pk=pk)
    else:
        cleaningServiceForm = CleaningServiceForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())
    context = {
        'form': form,
        'cleaningServiceForm': cleaningServiceForm,
        'title': 'Update Cleaning Service',
        'breadcrumb': 'Cleaning Service',
    }
    return render(request, 'adminControl/cleaningService/updateCleaningService.html', context=context)

@login_required
def deleteCleaningService(request , pk):
    instance = CleaningService.objects.get(pk=pk)
    instance.delete()
    messages.success(request, 'Cleaning Service Deleted Successfully')
    return redirect('showCleaningService')