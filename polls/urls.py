from django.urls import path

# importing views.py from root
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]