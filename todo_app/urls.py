from django.urls import path
from . import views


urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('revert_completed_task/<int:task_id>/', views.revert_completed_task, name='revert_completed_task'),
]