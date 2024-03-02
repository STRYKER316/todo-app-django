from django.shortcuts import render

from todo_app.models import Task


def home(request):
    pendingTasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completedTasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'pendingTasks': pendingTasks,
        'completedTasks': completedTasks,
    }
    return render(request, 'home.html', context)