from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def add_task(request):
    print(request.POST['task_form'])
    return HttpResponse('Form submitted and Task added')