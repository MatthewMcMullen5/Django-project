from django.urls import path
from pages.views import home_view

# url configuration or URLConf
urlpatterns = [
    path('', home_view, name='pages home'),

]