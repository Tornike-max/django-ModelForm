from django.urls import path

from . import views
urlpatterns = [
    path('',views.list_users,name='user-list'),
    path('add/', views.add_user, name='user-add'),
]