from django.urls import path
from . import views


urlpatterns = [
    # Add a new task
    path('add_task/', views.add_task, name='add_task'),
    # Mark a pending task as completed
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    # Mark a completed task as pending
    path('revert_completed_task/<int:task_id>/', views.revert_completed_task, name='revert_completed_task'),
    # Delete a task
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    # Edit a task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]