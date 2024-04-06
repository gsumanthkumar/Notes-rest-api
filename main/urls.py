from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('task-create/',views.taskcreate,name='taskpost'),
    path('task-list/',views.taskList,name='taskList'),
    path('task-detail/<str:pk>/',views.taskdetail,name='taskdetail'),
    path('task-edit/<str:pk>/',views.taskedit,name='taskedit'),
    path('task-delete/<str:pk>/',views.taskdelete,name='taskdelete')
]