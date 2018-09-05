from django.shortcuts import render
from app.comm import GlobalValue

# Create your views here.
def hello(request):

	value=10

	return render(request,'test.html',{'value':value})

def SendCmd(request):

	ClientMark=GlobalValue()

	ClientMark.set(connetmark=True)

	firstname = request.GET.get('firstname')

	lastname  = request.GET.get('lastname')

	return render(request,'sendcmd.html',{'firstname':firstname,'lastname':lastname})