from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.Top.as_view(), name='Top'),
    path('thanks/', views.Thanks.as_view(), name='thanks')
]