from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiselect_form, name='multiselect_form'),
    path('list/', views.error_list,name='error_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new, name='post_new'),
]