from django.shortcuts import render, redirect
from tasks.forms import TaskStoreForm
from tasks.models import TaskStoreModel

# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_task(request):
    if request.method == 'POST':
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            # print(task.cleaned_data)
            task.save()
            return redirect('show_tasks')

    else:
        task = TaskStoreForm()
    return render(request, 'addTask.html', {'form': task})


def show_tasks(request):
    task = TaskStoreModel.objects.all()
    print(task)
    return render(request, 'showTask.html', {'data':task})


def complete_tasks(request):
    task = TaskStoreModel.objects.all()
    print(task)
    return render(request, 'completeTask.html', {'data':task})


def edit_task(request, id):
    task = TaskStoreModel.objects.get(pk = id)
    form = TaskStoreForm(instance=task)
    if request.method == 'POST':
        task = TaskStoreForm(request.POST, instance=task)
        if task.is_valid():
            task.save()
            return redirect('show_tasks')

    else:
        task = TaskStoreForm()
    return render (request, 'edit_task.html', {'form':form})

def delete_task(request, id):
    task = TaskStoreModel.objects.get(pk = id).delete()
    return redirect('show_tasks')



def completed_task(request, id):
    task = TaskStoreModel.objects.get(pk=id)
    print(task)
    print("Task Details Before Deletion:")
    print("ID:", task.id)
    print("Title:", task.taskTitle)
    print("Description:", task.taskDescription)
    print("Status:", task.isCompleted)
    task = TaskStoreModel.objects.get(pk = id).delete()
    return render(request, 'completedTask.html', {'task': task})



