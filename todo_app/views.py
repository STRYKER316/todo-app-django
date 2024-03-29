from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


# create a new task
def add_task(request):
    task = request.POST['task_form']
    Task.objects.create(description=task)
    
    return redirect('home')


# Mark a pending task as completed
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = True
    task.save()
    
    return redirect('home')


# Mark a completed task as pending
def revert_completed_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    
    return redirect('home')


# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    
    return redirect('home')


# Edit a task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.description = request.POST['edit_task_form']
        task.save()
        return redirect('home')

    if request.method == 'GET':
        context = {
            'task': task,
        }
        return render(request, 'edit_task.html', context)
