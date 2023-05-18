from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task_3 import views

router = DefaultRouter()
router.register('product', views.ProductModelViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
