from django.urls import path
from .views import SheetsDataListView

urlpatterns = [
    path('', SheetsDataListView.as_view())
]
