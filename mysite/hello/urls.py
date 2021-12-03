from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.times_visited, name='index'),

]