from django.urls import path
from .views import home, submit_result

urlpatterns = [
    path("", home, name="home"),
    path("submit/", submit_result, name="submit_result"),
] 