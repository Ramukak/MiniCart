from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import *
import random
import http.client,requests
from django.conf import settings

#helper funtions

import requests
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Profile

def send_otp(mobile, otp):
    auth_key = "413210AXy6nZWwl659b6b3aP1"
    sender_id = "vivek25"
    template_id = '659b73b8d6fc050c226351d4'  # Replace with the actual template ID
    url = f"https://control.msg91.com/api/v5/otp?template_id={template_id}&mobile={mobile}&otp={otp}&otp_length=4"
    payload = {
        "otp": f"{otp}"
    }

    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authkey": f"{auth_key}"
    }
    requests.post(url, json=payload,headers=headers)
    

    

def registerUser(request):
    if request.method == "POST":
        name = request.POST.get('registerName')
        email = request.POST.get('registerEmail')
        phone = request.POST.get('phonenumber')
        check_user = Profile.objects.filter(mobile=phone).first()
        if check_user:
            context = {'message': 'Mobile already taken', 'class': 'danger'}
            return render(request, 'login.html', context)

        user = User(email=email, username=name)
        user.save()

        otp = str(random.randint(1000, 9999))
        profile = Profile(user=user, mobile=phone, otp=otp)
        profile.save()

        request.session['mobile'] = phone

        # Send OTP and check if it was successful
        send_otp(phone, otp)
        return redirect('otp')
        

    return redirect('index')

# Create your views here.
def index(request):
    return render(request,'login.html')

def loginUser(request):
    pass



def otpView(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    return render(request,'otp.html',context)