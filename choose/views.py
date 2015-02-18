import json
import time
from random import random
from django.shortcuts import render
from choose.models import Choices,Rolls
from django.core.context_processors import csrf
from django.http import HttpResponse

from choose.forms import GetChoiceForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = GetChoiceForm(request.POST)
        if form.is_valid():
            Choices(choice=form.cleaned_data['choiceField'], ip=request.META.get('REMOTE_ADDR')).save()
    
    form = GetChoiceForm()
    return render(request, 'chooseBase.html', {'form':form})

def checkChoices(request):
    responseData = {}
    largest=-1
    for x in list(Choices.objects.filter(trigger=1, id__gt=request.GET.get('index', '[]'))):
        responseData[x.id]=x.choice
        if x.id > largest:
            largest=x.id
    responseData['largest']=largest
    return HttpResponse(json.dumps(responseData))


def loadRoll(request):
    if not Rolls.objects.filter(trigger=1):
        choices = Choices.objects.filter(trigger=1)
        choiceAmt = len(choices)
        Rolls(start=0, end=0, randomRoll=((random()*1000)%choiceAmt)).save()
        time.sleep(10)
        Rolls.objects.filter(trigger=1).update(trigger=0)
        choices.update(trigger=0)
        return HttpResponse(1)
    else:
        return HttpResponse(0)
    
def getRoll(request):
    triggerAlert = Rolls.objects.filter(trigger=1)
    if triggerAlert:
        return HttpResponse(json.dumps(triggerAlert[0].randomRoll))
    else:
        return HttpResponse(-1)

def refresh(request):
    time.sleep(10)
    return HttpResponse(1)
    
    
    