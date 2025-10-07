from django.urls import path
from .views import PublisherListCreateView, PublisherDetailView

app_name = "publishers"

urlpatterns = [
    path("", PublisherListCreateView.as_view(), name="publisher-list"),
    path("<int:pk>/", PublisherDetailView.as_view(), name="publisher-detail"),
]
