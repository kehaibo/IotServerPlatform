#coding:utf-8
from django.shortcuts import HttpResponse,render,redirect

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from .TcpClient import StartClientThread

host = '192.168.3.13'

port = 8001

# Create your views here.
def hello(request):

	value=10

	return render(request,'test.html',{'value':value})

@login_required  
def StartConnect(request):

	global host
	global port

	status=StartClientThread(host,port)

	return render(request,'test.html',{'host':host,'port':port,'status':status})

def UserLogin(request):


	if request.method == "POST":
		
		username = request.POST.get("username")

		password = request.POST.get("password")

		print(str(password)+str(username))

		user = authenticate(username=username,password=password)

		if user is not None and user.is_active:

			login(request,user)

			return redirect('/login/home')

		else :

			return HttpResponse('login failuer!')

	return render(request,"login.html")

	

def acc_logout(request):

	logout(request)

	return redirect("/login")

