from django.urls import path
from . import views
app_name = 'library'
urlpatterns = [ path('', views.library_home, name='library_home'), ]
