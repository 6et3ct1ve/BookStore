from django.urls import path
from .views import PublisherListCreateView, PublisherDetailView
from books.views import PublisherBooksView

app_name = 'publishers'

urlpatterns = [
    path('', PublisherListCreateView.as_view(), name='publisher-list-create'),
    path('<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('<int:publisher_id>/books/', PublisherBooksView.as_view(), name='publisher-books'),
]
