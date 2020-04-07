from django.urls import path

from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
]

router = routers.DefaultRouter()
router.register(r'iris', views.IrisViewSet)