from django.urls import path
from .views import subnetzoneview

urlpatterns = [
    path('subnets/', subnetzoneview.as_view(), name='subnetzoneview'),
]
