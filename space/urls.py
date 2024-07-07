from django.urls import path
from . import views

urlpatterns = [
    path('actualurl/', views.view_func),
    path('', views.index, name="index"),
    path('<int:id>', views.details, name="details")
]
