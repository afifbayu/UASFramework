# crud_app/urls.py
from django.urls import path
from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView

urlpatterns = [
    
    path('items/', ItemListCreateView.as_view(), name='api-root'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-retrieve-update-destroy'),
]
