from django.http import HttpResponse
from django.shortcuts import render
from App.models import *


def INDEX(request):
    
    return render(request, '../templates/index.html', locals())


def slotbooking(request):
    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)
    state = None
    district = None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        print(getcountry.name)
        state = State.objects.filter(country=getcountry)
        
    if stateid:
        getstate = State.objects.get(id=stateid)
        print(getstate.name)
        district = District.objects.filter(state=getstate)
    
    country = Country.objects.all()
    
    return render(request, '../templates/sample.html', locals())

def payments(request):
    countryid = request.GET.get('country', None)

    stateid = request.GET.get('state', None)
    mandalid = request.GET.get('district', None)
    state = None
    district = None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        state = State.objects.filter(country=getcountry)

    if stateid:
        getstate = State.objects.get(id=stateid)
        district = District.objects.filter(state=getstate)
    if stateid:
        getstate = District.objects.get(id=stateid)
        district = District.objects.filter(state=getstate)

    return render(request,'../templates/payment.html')