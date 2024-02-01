from django.urls import path
from . import views

urlpatterns = [
    path('api_data/', views.ApiDataListView.as_view()),
    path('api_data/<int:id>', views.ApiDataListView.as_view()),
]
