from django.conf.urls import include, url
from django.urls import path
from . import views

#urlpatterns = [
    #
#]

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.post_list),
]