from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task


# Create your views here.
def add_task(request):
    task = request.POST['task_form']
    Task.objects.create(description=task)
    
    return redirect('home')
