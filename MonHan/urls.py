from django.urls import path
from . import views
from .views import CreateMyModelView

app_name = 'MonHan'
urlpatterns = [
    #path('', views.monster_list, name='monster_list'),
    path('', CreateMyModelView.as_view()),
    path('', views.index, name='index'),
]