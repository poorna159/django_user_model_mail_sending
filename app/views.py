from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def registration(request):
    usfo=UserForm()
    pfo=ProfileModelForm()
    d={'usfo':usfo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        usfd=UserForm(request.POST)
        pfd=ProfileModelForm(request.POST,request.FILES)

        if usfd.is_valid() and pfd.is_valid():
            NSUFO=usfd.save(commit=False)
            submittedPW=usfd.cleaned_data['password']
            NSUFO.set_password(submittedPW)
            NSUFO.save()

            NSPO=pfd.save(commit=False)
            NSPO.username=NSUFO
            NSPO.save()

            send_mail('Registration','hai hello ',
                        'poorna.p159@gmail.com',
                        [NSUFO.email],
                        fail_silently=False)

            return HttpResponse('registration successful')

    return render(request,'registration.html',d)
