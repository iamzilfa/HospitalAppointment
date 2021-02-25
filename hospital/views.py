from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


# def admin_signup_view(request):
#     form=AdminSignupForm()
#     if request.method=='POST':
#         form=AdminSignupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()
#             newadmin=AdminProfile(user=user)
#             return redirect ('registration/login.html')
#     return render(request,'registration/registration_form.html',{'form':form})

