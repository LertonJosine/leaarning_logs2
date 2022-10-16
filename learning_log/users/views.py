from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def my_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def registrar(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            autenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, autenticated_user)
            return HttpResponseRedirect(reverse('home'))
    context = {'form':form}
    return render(request, 'registration/register.html', context)