from django.shortcuts import render

from django.template.response import TemplateResponse
from station.models import Reading

def home(request):
    data = Reading.objects.last()
    #data = Reading.objects.all()

    return TemplateResponse(request, 'index.html', {'data': data})


