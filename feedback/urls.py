from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.FeedbackListView.as_view(), name='list'),
    path('add/', views.FeedbackCreateView.as_view(), name='add'),
]
