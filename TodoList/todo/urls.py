from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('todo/<int:pk>/', TodosAPIView.as_view()),
]