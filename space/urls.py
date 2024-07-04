from django.urls import path
from . import views

urlpatterns = [
    path('actualurl/', views.view_func)
]
