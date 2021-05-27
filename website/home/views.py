from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


def HomeView(request):
    tasks = ListToDo.objects.all()
    taskforms = TaskForm()
    if request.method == 'POST':
        taskforms = TaskForm(request.POST)
        if taskforms.is_valid():
            taskforms.save()
        return redirect('/')
    konteks = {
        'judul': 'home',
        'taskforms': taskforms,
        'tasks': tasks,
    }
    return render(request, 'index.html', konteks)


def UpdateView(request, pk):
    task = ListToDo.objects.get(id=pk)
    taskforms = TaskForm(instance=task)
    konteks = {
        'judul': 'update',
        'taskforms': taskforms,
    }
    if request.method == 'POST':
        taskforms = TaskForm(request.POST, instance=task)
        if taskforms.is_valid():
            taskforms.save()
        return redirect('/')

    return render(request, 'update.html', konteks)


def DeleteView(request, pk):
    task = ListToDo.objects.get(id=pk)
    konteks = {
        'judul': 'Delete Confirmation',
        'task': task,
    }

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'delete.html', konteks)
