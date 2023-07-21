from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def registration(request):
    usfo=UserForm()#user_form_object
    pfo=ProfileModelForm()#profile_form_object
    d={'usfo':usfo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        #when we are dealing with both data and files(images)
        usfd=UserForm(request.POST)
        #Formobject returned with some data that we are collecting and storing in USFD
        pfd=ProfileModelForm(request.POST,request.FILES)
        #profile form is dealing with both data and files
        if usfd.is_valid() and pfd.is_valid():
            NSUFO=usfd.save(commit=False)#by default it will be true
            #it will return a not saved userform object
            submittedPW=usfd.cleaned_data['password']
            NSUFO.set_password(submittedPW)
            #performing encrypt password operation by using set_password method
            NSUFO.save()

            NSPO=pfd.save(commit=False)
            #want to add a username column for that we are providing an object as value
            NSPO.username=NSUFO
            NSPO.save()

            send_mail('Registration','hai hello prasanna ',
                        'poorna.p159@gmail.com',
                        [NSUFO.email],
                        fail_silently=False)

            return HttpResponse('Registration is successfull')
        

    return render(request,'registration.html',d)
