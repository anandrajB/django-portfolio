from django.shortcuts import render
from app.models import contact , files
from django.http import HttpResponse, request
from django.conf import settings
import os
import time
from time import sleep
from datetime import date
import datetime
from django.http import Http404 , HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from rest_framework import response


# Create your views here.



def index(request):
	context = {'file': files.objects.all()}
	return render(request,'app/index.html',context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        date_now = date.today()
        when = datetime.datetime.today().strftime('%A')
        data = {
            'name' : name,
            'email' : email,
            "message" : message,
            'date_n' : date_now,
            'when' : when,
        }
        message = '''
        Hey Anand ! 
        
        You Got a message on {} / {}
        
        From : {}

        Name : {}

        Message : {}
        
        '''.format(data['date_n'],data['when'],data['email'],data['name'],data['message'])
        #sender from settings.email to [receiver]
        send_mail(data['name'], message, data['email'],['anand98.ar@gmail.com'],fail_silently=False,)
        messages.success(request , 'Thank you ! we will get u back shortly , Have a good day')
        return HttpResponseRedirect('/')
    return render(request,'app/others/contact.html')

def resume(request):
	return render(request,'app/others/myresume.html')

def portfolio(request):
	return render(request,'app/others/portfolio-details.html')

def maintanace_mode(request):
    return render(request,'app/others/503.html')

def handler404(request, exception):
    return render(request,'app/404.html')