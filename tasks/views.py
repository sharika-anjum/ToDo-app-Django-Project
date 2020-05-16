from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages,auth

from .models import *
from .forms import *

# Create your views here.

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'list.html', context)


def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'delete.html', context)

def mainpage(request):
    return render(request,"login.html")

def mainpage1(request):
    return render(request,"register.html")

def aboutus(request):
    return render(request,"About us.html")
def insert(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/main")
            except:
                pass
    else:
        form=UserForm()
    return render(request,'register.html',{'form':form})

def reg(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def log_check(request):
    if request.method=="POST":

        name = request.POST['name']
        pwd = request.POST['pwd']
        try:
            u=user.objects.get(name=name,pwd=pwd)
            if u is not None:
                return redirect("/")


            else:
                messages.info(request,'INVALID CREDENTIALS!')
                return redirect("/main")
        except:
            messages.info(request, 'INVALID CREDENTIALS!')
            return redirect("/main")
    else:
        return render(request,'login.html')




