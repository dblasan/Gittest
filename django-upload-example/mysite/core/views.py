from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import requests
import sys
from subprocess import run,PIPE


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def external(request):
     inp= request.POST.get('param')
     out= run([sys.executable,'//home//developer//Downloads//RechteGanzeBein.py',inp],shell=False,stdout=PIPE)
     print(out)
     return render(request,'upload.html',{'data1':out.stdout})