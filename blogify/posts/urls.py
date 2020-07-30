from django.urls import path
from . import views


app_name = "posts" # namespace

urlpatterns = [
    path('', views.post_list, name="list"),
    path('<slug:slug>/', views.post_detail, name="detail"),
]
