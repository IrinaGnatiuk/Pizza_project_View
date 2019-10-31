from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderView.as_view()),
    path('', views.MyView.as_view()),
    path('', views.AboutView.as_view()),

]