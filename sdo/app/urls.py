from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('cycles/', views.cycles_list, name='cycles_list'),
    path('groups/', views.groups_list, name='groups_list'),
]
