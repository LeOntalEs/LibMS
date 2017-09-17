from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def login(request):
    if request.method == 'POST':
        print('post', request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usr = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=usr, password=pwd)
            print(user)
            if not user is None:
                auth_login(request, user)
                return HttpResponseRedirect(request.POST.get('next', '/'))
            else:
                return HttpResponse(status=400)
    else:
        context = {'form': AuthenticationForm(request)}
        return render(request, 'login.html', context)