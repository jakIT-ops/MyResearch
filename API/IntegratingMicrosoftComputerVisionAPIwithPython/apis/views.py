from apis.models import Key_Endpoint, OCR, ImageAnalysis2
from .forms import OCRForm, ImageAnalysis2Form
from django.shortcuts import render, redirect
import requests

# Create your views here.

def index(request):
    return render(request, 'apis/index.html')

def ocr(request):
    key_endpoint = Key_Endpoint.objects.all()
    done = "Please enter endpoint and subscription_key"
    data = ""
    img = ""

    if key_endpoint != None:
        key_endpoint = key_endpoint.last()
        done = "You have added the endpoint and subscription_key"

    if request.method != 'POST':
        form = OCRForm()
    else:
        form = OCRForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            obj = OCR()
            img = form.cleaned_data['image_url']
            obj.set_url(img)
            k_e = Key_Endpoint()
            k_e.set_endpoint("{{ENDPOINT}}")
            k_e.set_key("{{SUBSCRIPTION_KEY}}")
            data = obj.ocr(k_e)
    
    context = {"keys_status": done, "form": form, "data": data, "image":img}
    return render(request, 'apis/ocr.html',context)

def imageanalysis(request):
    key_endpoint = Key_Endpoint.objects.all()
    done = "Please enter endpoint and subscription_key"
    data = ""
    img = ""
    if key_endpoint != None:
        key_endpoint = key_endpoint.last()
        done = "You have added the endpoint and subscription_key"

    if request.method != 'POST':
        form = ImageAnalysis2Form()
    else:
        form = ImageAnalysis2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.cleaned_data['image_url']
            obj = ImageAnalysis2()
            obj.set_url(form.cleaned_data['image_url'])
            obj.set_process(form.cleaned_data['select'])
            k_e = Key_Endpoint()
            k_e.set_endpoint("{{ENDPOINT}}")
            k_e.set_key("{{SUBSCRIPTION_KEY}}")
            data = obj.analyse(k_e)
    
    context = {"keys_status": done,"data": data,"form": form, "image": img}

    return render(request, 'apis/imageanalysis.html', context)