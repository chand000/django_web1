# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, redirect,HttpResponse

from django.contrib.auth import login as auth_login

from django.contrib.auth import authenticate , logout 
from django.contrib.auth import logout as django_logout


from django.contrib.auth.models import User 

from .models import Contact ,Signup

from django.contrib import messages



def home(request) :
    messages.add_message(request, messages.INFO, 'Welcome there....')
    return render(request,'home.html' , {'titles':'home'})
  
        
    # return HttpResponse("hello world")

def contact(request) :
    username = request.POST['username']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    print(username,'\n',email,'\n',subject,'\n',message,'\n')
    user = Contact(username=username,email = email, subject=subject, message= message)
    user.save()
    messages.success(request,'contact send')
    print('User Created')
    return redirect('/')

def signup(request) :
    if request.method == 'POST':
        # username = request.POST['username']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # repass = request.POST['repass']

        print(username,'\n',email,'\n',password,'\n')
        user = User(username =username,email = email, password= password)
        user.save()
        messages.success(request,'User created')
        print('User Created')
        return redirect('/')
    else:
        return render(request,'signup.html' , {'titles':'signup'})

def login(request) :
    if request.method=="POST":
        # username = Signup(username='username')
        # email = Signup(email='email')
        # password = Signup(username='password')

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        user = authenticate(username=username, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            print("Succesfully Logged In...........................................................")
            messages.success(request,'Succesfully Logged In')
            return redirect('/')
        else:
            print("invalid Logged In...........................................................")
            messages.error(request,'invalid credetials')
            return render(request,'login.html' , {'titles':'login'})


    return render(request,'login.html' , {'titles':'login'})



def logout(request):
    django_logout(request)
    print("logout...........................................................")
    messages.success(request, "Successfully logged out")
    return redirect('/')


def linkedin(request) :
    return render(request,'linkedin.html' , {'titles':'linkedin'})

def twitter(request) :
    return render(request,'twitter.html' , {'titles':'twitter'})

def facebook(request) :
    return render(request,'facebook.html' , {'titles':'facebook'})

def instagram(request) :
    return render(request,'instagram.html' , {'titles':'instagram'})

def github(request) :
    return render(request,'github.html' , {'titles':'github'})

# def gmail(request) :
#     import smtplib

#     gmail_user = 'singhchandni000@gmail.com'
#     gmail_password = 'chandni1212'

#     sent_from = gmail_user
#     to = ['singhchandni000@gmail.com']
#     subject = 'OMG Super Important Message'
#     body = 'Hey, whats up?\n\n- You'

#     email_text = """\
#     From: %s
#     To: %s
#     Subject: %s
#     %s
#     """ % (sent_from, ", ".join(to), subject, body)
#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.ehlo()
#         server.login(gmail_user, gmail_password)
#         server.sendmail(sent_from, to, email_text)
#         server.close()
#         print('Email send')
#     except:
#         print ('Something went wrong...')
    
#     return render(request,'home.html' , {'titles':'github'})
