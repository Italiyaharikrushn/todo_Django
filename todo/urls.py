from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('AddTask/',views.addTask,name='add'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.editTask, name='edit_task'),
]
