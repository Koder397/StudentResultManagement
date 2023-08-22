from django.urls import path

from frontend.views import login

urlpatterns = [
    path('', login),
]