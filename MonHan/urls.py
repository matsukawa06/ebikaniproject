from django.urls import path
from . import views

app_name = 'MonHan'

urlpatterns = [
    path('', views.monster_list.as_view(), name='monster_list'),
]