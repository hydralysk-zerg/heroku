from django.urls import path
from django.urls.conf import include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("test2/", views.index_test2, name="index_test"),
    ]
