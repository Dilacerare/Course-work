from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('cycles/', views.cycles_list, name='cycles_list'),
    path('cycles/add', views.cycles_add, name='cycles_add'),
    path('cycles/delete/<int:id>', views.cycles_delete, name='cycles_delete'),
    path('groups/', views.groups_list, name='groups_list'),
    path('groups/add', views.groups_add, name='groups_add'),
    path('groups/delete/<int:id>', views.groups_delete, name='groups_delete'),
]
