from django.urls import path
from cashbook import api

app_name = 'cashbook'

urlpatterns = [
    path('', api.MovementList.as_view(), name='list'),
    path('<int:pk>/',
         api.MovementDetail.as_view(), name='detail'),
]
