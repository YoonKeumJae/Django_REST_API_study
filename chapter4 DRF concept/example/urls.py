from django.urls import path, include
from .views import HelloAPI, booksAPI, bookAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("books/", booksAPI),
    path("book/<int:bid>/", bookAPI)
]