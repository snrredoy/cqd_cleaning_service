from django.shortcuts import render , redirect 
from django.contrib import messages
from .models import CQDAdvantage , CQDAdvantageSection
from adminControl.models import General
from .forms import CQDAdvantageForm , CQDAdvantageSectionForm
from adminControl.forms import GeneralForm

# Create your views here.
def showCQDAdvantage(request):
    form = GeneralForm(instance=General.objects.first())
    cqdAdvantageSection = CQDAdvantageSection.objects.first()
    cqdAdvantage = CQDAdvantage.objects.all()

    context = {
        'form': form,
        'cqdAdvantageSection': cqdAdvantageSection,
        'cqdAdvantages': cqdAdvantage,
        'title': 'CQD Advantage',
        'breadcrumb': 'CQD Advantage',
    }

    return render(request, 'adminControl/cqdAdvantage/showCQDAdvantage.html', context=context)

def updateCQDAdvantageSection(request , pk):
    instance = CQDAdvantageSection.objects.get(pk=pk)
    if request.method == 'POST':
        cqdAdvantageSectionForm = CQDAdvantageSectionForm(request.POST , instance=instance)
        if cqdAdvantageSectionForm.is_valid():
            cqdAdvantageSectionForm.save()
            messages.success(request, 'CQD Advantage Section Updated Successfully')
            return redirect('showCQDAdvantage')
        else:
            messages.error(request, 'Please check the form again.')
            return redirect('updateCQDAdvantageSection' , pk=pk)
    else:
        cqdAdvantageSectionForm = CQDAdvantageSectionForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'cqdAdvantageSectionForm': cqdAdvantageSectionForm,
        'title': 'Update CQD Advantage Section',
        'breadcrumb': 'CQD Advantage',
    }

    return render(request, 'adminControl/cqdAdvantage/updateCQDAdvantageSection.html', context=context)

def addCQDAdvantage(request):
    if request.method == 'POST':
        cqdAdvantageForm = CQDAdvantageForm(request.POST , request.FILES)
        if cqdAdvantageForm.is_valid():
            cqdAdvantageForm.save()
            messages.success(request, 'CQD Advantage Added Successfully')
            return redirect('showCQDAdvantage')
        else:
            messages.error(request, 'Please check the form again.')
            return redirect('addCQDAdvantage')
    else:
        cqdAdvantageForm = CQDAdvantageForm()

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'cqdAdvantageForm': cqdAdvantageForm,
        'title': 'Add CQD Advantage',
        'breadcrumb': 'CQD Advantage',
    }

    return render(request, 'adminControl/cqdAdvantage/addCQDAdvantage.html', context=context)

def updateCQDAdvantage(request , pk):
    instance = CQDAdvantage.objects.get(pk=pk)
    if request.method == 'POST':
        cqdAdvantageForm = CQDAdvantageForm(request.POST , request.FILES , instance=instance)
        if cqdAdvantageForm.is_valid():
            cqdAdvantageForm.save()
            messages.success(request, 'CQD Advantage Updated Successfully')
            return redirect('showCQDAdvantage')
        else:
            messages.error(request, 'Please check the form again.')
            return redirect('updateCQDAdvantage' , pk=pk)
    else:
        cqdAdvantageForm = CQDAdvantageForm(instance=instance)

    form = GeneralForm(instance=General.objects.first())

    context = {
        'form': form,
        'cqdAdvantageForm': cqdAdvantageForm,
        'title': 'Update CQD Advantage',
        'breadcrumb': 'CQD Advantage',
    }

    return render(request, 'adminControl/cqdAdvantage/updateCQDAdvantage.html', context=context)

def deleteCQDAdvantage(request , pk):
    instance = CQDAdvantage.objects.get(pk=pk)
    instance.delete()
    messages.success(request, 'CQD Advantage Deleted Successfully')
    return redirect('showCQDAdvantage')

