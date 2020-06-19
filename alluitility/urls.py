from django.urls import path
from .import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.index, name='index'),  #  rendering ide page
    path('plag', views.ide, name='plag'),   #  response to ide
]
