from django.urls import path
from task_9 import views

urlpatterns = [
    path('third-party/', views.ThirdPartyAPIView.as_view()),
]
