from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:course_id>/delete', views.delete),
    path('<int:course_id>/delete_confirm', views.delete_confirm)
]
