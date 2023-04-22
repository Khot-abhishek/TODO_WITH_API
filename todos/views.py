from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def task_list(request):
    task_list = Task.objects.all()
    return render(request, 'todos/task_list.html', {'task_list':task_list})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user_id = request.user.id
            new_task.save()
        return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'todos/task_create.html',{'form':form})


def task_update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        return render(request, 'todos/task_update.html',{'form':form})


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')