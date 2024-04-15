from django.urls import path

from task_manager.statuses import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='statuses'),
    path('create/', views.StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', views.StatusUpdate.as_view(),
         name='status_update'),
    path('<int:pk>/delete/', views.StatusDelete.as_view(),
         name='status_delete'),
]
