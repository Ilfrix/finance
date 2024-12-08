from django.urls import path

from . import views

app_name = 'wallet'

urlpatterns = [
    path('', views.money, name='money'),
    path('<int:pk>/', views.money, name='money'),
    path('update/', views.update_info, name='update'),
]
