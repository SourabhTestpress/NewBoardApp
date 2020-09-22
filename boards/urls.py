from django.urls import path
from . import views

urlpatterns = [
    path('',views.board_list,name="home"),
    path('board/<str:slug>/',views.board_details,name="board_details"),
]