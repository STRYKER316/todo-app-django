from django.shortcuts import get_object_or_404, redirect

from .models import Task


# Create your views here.
def add_task(request):
    task = request.POST['task_form']
    Task.objects.create(description=task)
    
    return redirect('home')


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = True
    task.save()
    
    return redirect('home')
