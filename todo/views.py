from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):

	#model initializer
	tasks = Task.objects.all()

	if request.method == 'POST':
		#add values to form if method == POST
		form = TaskForm(request.POST or none)
		if form.is_valid():
			form.save()
		return redirect('home')

	#form initializer
	form = TaskForm() 
	context = {
		'tasks': tasks,
		'form' : form,
		}
	return render(request, 'home.html', context) 

def edit(request, pk):
	
	#model initializer --> specific indexed
	task = Task.objects.get(id=pk)

	#form initializer --> specific indexed
	#this will pre-fill the form 
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
		return redirect('home')

	context = {
		'task': task,
		'form': form,
		}
	return render(request, 'edit.html', context)

def delete(request, pk):

	#model initializer
	task = Task.objects.get(id=pk)
	if request.method == 'POST':
			task.delete()
			return redirect('home')
	context = {
		'tasks':task,
	}
	return render(request, 'delete.html', context)
