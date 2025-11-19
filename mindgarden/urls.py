from django.urls import path
from . import views

app_name = "mindgarden"

urlpatterns = [
    path("", views.mind_home, name="mind_home"),
]
