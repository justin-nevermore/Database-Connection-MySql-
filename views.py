from django.shortcuts import render
from .models import Reg
from .forms import RegistrationDetails, CheckLogin
from django.contrib import messages
from django.http import HttpResponse
from .databaselayer import databaselayer as da

import mysql.connector

def index(request):
    # Main Page (redirects to the main page ("base")

    if request.method=='POST':
        form = CheckLogin(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['username']
            Password = form.cleaned_data['password']
            db = mysql.connector.connect(user='root', password='root', host='10.11.20.58')
            cur = db.cursor()
            cur.execute('select * from django.l_reg where username="' + Username + '" and pssword="'+Password+'"')
            ob = cur.fetchall()


            if len(ob) > 0: #[(2, 'JUSTIN', 'JAGDEEP', 'tambaram', '25', 'justinjagdeep.ar@ptechnosoft.c', 'AAA')]
                stri="<br>Name :"+ob[0][1]+" "+ob[0][2]+"<br> Location :"+ob[0][3]+"<br> Age :"+ob[0][4]
                return HttpResponse("done{}".format(stri))
            else:
                return HttpResponse("not done")
    form = CheckLogin()

    return render(request, 'base.html', {'form': form})


def login(request):

    # Redirects to the registers's details page

    return render(request, 'display.html')


def registration(request):
    # Redirects to the form filling page

    if request.method == 'POST':
        form = RegistrationDetails(request.POST)
        if form.is_valid():
            # form.save()
            # messages.success(request, 'Registration Successfull')

            fname = form.cleaned_data['firstname']
            lname = form.cleaned_data['lastname']
            loc = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            da.registration(fname, lname, loc, age, username, password)

            # register=Reg(firstname=fname, lastname=lname, location=loc, age=age, username=username, pssword=password)
            # register.save()


    form = RegistrationDetails()

    return render(request, 'registration.html', {'form': form})


#"insert into django.l_reg (firstname,lastname,location,age,username,password) values ('justin''ar''ar''22''lol''lol')"