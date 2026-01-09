from django.shortcuts import render
from .models import *


def Home(req):
    return render(req, 'Home.html')


def Register(req):
    if req.method == 'POST':
        nm = req.POST['na']
        em = req.POST['ew']
        pw = req.POST['pq']
        pw1 = req.POST['pq1']

        if pw != pw1:
            Error = 'Both Password Should Be Match !!'
            return render(req, 'Register.html', context={'Err': Error})

        vb = Users.objects.filter(Email=em).count()
        if vb == 1:
            Error = 'Email Already Exists !!'
            return render(req, 'Register.html', context={'Err': Error})

        else:
            ob = Users(Name=nm, Email=em, Password=pw)
            ob.save()
            return render(req, 'Home.html')
    else:
        return render(req, 'Register.html')