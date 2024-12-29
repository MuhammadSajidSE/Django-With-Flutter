from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a view for the root URL
    path('hello/', views.hello, name='hello'),  # Define a view for the /hello/ URL
]
