from django.urls import path
from .views import Mongo_User
urlpatterns = [
    path('', Mongo_User.as_view()),
]