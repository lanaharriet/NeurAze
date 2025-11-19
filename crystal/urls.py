from django.urls import path
from . import views
app_name = 'crystal'
urlpatterns = [ path('', views.crystal_home, name='crystal_home'), ]
