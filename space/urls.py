from django.urls import path
from . import views

app_name = "space"
urlpatterns = [
    path('actualurl/', views.view_func),
    path('<int:id>/addSatellite', views.addSatellite, name="addSatellite"),

    path('<int:id>', views.details, name="details"),
    path('', views.index, name="index"),
]
