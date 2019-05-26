from django.urls import path
from .views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='taks-list'),
#   path('<int:task_id>/', views.detail, name='detail'),
]
