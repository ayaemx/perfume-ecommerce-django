from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name='list'),
    path('add/', views.CategoryCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete'),
]
