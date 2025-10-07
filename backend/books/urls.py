from django.urls import path
from .views import BookListCreateView, BookDetailView, PublisherBooksView

app_name = "books"

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path(
        "publishers/<int:publisher_id>/books/",
        PublisherBooksView.as_view(),
        name="publisher-books",
    ),
]
