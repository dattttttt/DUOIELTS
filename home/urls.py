from django.urls import include, path

from .views import *

urlpatterns = [
    path("", TaskView.as_view(), name="index"),
]