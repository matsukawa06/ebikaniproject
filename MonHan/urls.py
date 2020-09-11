from django.urls import path
from . import views

app_name = 'MonHan'

urlpatterns = [
    path('', views.monster_list.as_view(), name='monster_list'),
    path('custom_list/', views.custom_list, name='custom_list'),
]