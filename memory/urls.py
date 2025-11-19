from django.urls import path
from . import views
app_name = 'memory'
urlpatterns = [ path('', views.memory_home, name='memory_home'), ]
