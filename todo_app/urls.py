from django.urls import path
from . import views


urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
]