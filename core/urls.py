from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('hello/<str:name>', views.hello),      # Dynamic URL
    path('add/<int:num1>/<int:num2>', views.add),
    path('multiply', views.mul)
]