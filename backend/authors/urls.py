from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView

app_name = "authors"

urlpatterns = [
    path("", AuthorListCreateView.as_view(), name="author-list"),
    path("<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]
