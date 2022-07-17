from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('greeting/', views.getgreeting, name='greetings'),
    path('add-greeting/', views.addgreeting, name='add greeting'),
    path('update-greeting/<str:pk>/', views.updategreeting, name='update greeting'),
    path('delete-greeting/<str:pk>/', views.deletegreeting, name='delete greeting'),
]
