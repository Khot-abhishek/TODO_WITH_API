from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt 


urlpatterns = [

    path('tasks/', views.get_task_list, name='api_task_list'),
    path('tasks/<int:pk>/', views.get_task_detail, name='api_task_detail'),
    path('create/', views.create_task, name='api_create_task'),
    path('delete/<int:pk>/', views.delete_task, name='api_delete_task'),
    path('update/<int:pk>/', views.update_task, name='api_update_task'),
    path('completed/<int:pk>/', views.completed, name='api_completed_task'),

]