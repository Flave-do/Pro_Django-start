from django.urls import path
from .views import User_Data
urlpatterns = [
    path('', User_Data.as_view()),
]
