from django.urls import path

from . import views

app_name = 'spending'

urlpatterns = [
    path('', views.all_spending, name='all_spending'),
    path('update/', views.update_info, name='update'),
    path('create/', views.create, name='create'),
    # path('<int:pk>/', views.money, name='spending'),
    # path('add/<int:pk>/', views.update_info, name='add_spend'),
]
