from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from .models import *
from .forms import *
from .utils import send_sms
from django.http import HttpResponse

# Create your views here. 

def Home(request):
    return render(request, 'Home.html')

def auth_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('/veryfy_view')
    return render(request,  'auth_view.html', {'form':form})        


def veryfy_view(request): 
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        Myuser = CUSTOMUSER.objects.get(pk=pk)

        code = CODE.objects.get(user__pk=pk)
        code_user = f"{Myuser.username}: {code}" 

        if not request.POST:
            print(str(code))
            send_sms(code_user, Myuser.Phone_No)

        if form.is_valid():
            num = form.cleaned_data.get('Number_Code')

            if str(code) == num:
                code.save()
                auth.login(request, Myuser)
                return HttpResponse(f"<h1> {Myuser.username} Logged in.</h1>")
            else:
                return redirect('/auth_view')
    return render(request, 'veryfy_view.html', {'form':form})   
