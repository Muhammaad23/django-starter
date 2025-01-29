from django.urls import path
from .views import *


urlpatterns = [
    path('', char_view, name='home'),
]