from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview, name='api-overview'),

    # Items
    path('get-item', views.getitem, name='get-item'),
    path('add-item/', views.additem, name='add-item'),
    path('update-item/<str:pk>/', views.updateitem, name='update-item'),
    path('delete-item/<str:pk>/', views.deleteitem, name='delete-item'),
    path('item-list/', views.itemlist, name='item-list'),
    path('item-detail/<str:pk>/', views.itemdetail, name='item-detail'),

    # Tasks
    path('get-task/', views.gettask, name='get-task'),
    path('add-task/', views.addtask, name='add-task'),
    path('update-task/<str:pk>/', views.updatetask, name='update-task'),
    path('delete-task/<str:pk>/', views.deletetask, name='delete-task'),
    path('task-list/', views.tasklist, name='task-list'),
    path('task-detail/<str:pk>/', views.taskdetail, name='task-detail'),

]
