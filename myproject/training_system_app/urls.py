from django.urls import path

from .views import ProductListView


app_name = 'training_system_app'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
]