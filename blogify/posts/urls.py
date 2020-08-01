from django.urls import path
from . import views


app_name = "posts" # namespace

urlpatterns = [
    path('', views.post_list, name="list"),
    path('create/', views.post_create, name="create"), # fires this url first instead of slug
    path('<slug:slug>/', views.post_detail, name="detail"),
]
