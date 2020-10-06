from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    thispassword=''
    rand_char=list("abcdefghijklmnopqrstuvwxyz")

    if(request.GET.get('Uppercase')):
        rand_char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if(request.GET.get('Special Characters')):
        rand_char.extend(list("!@#$%^&*(){}:;<>"))
    if(request.GET.get('Numbers')):
        rand_char.extend(list("0123456789"))
    length=int(request.GET.get('length',12))

    for item in range(length):
        thispassword+=random.choice(rand_char)
    return render(request,'generator/password.html',{'password':thispassword})

def about(request):
    return render(request,'generator/about.html')
