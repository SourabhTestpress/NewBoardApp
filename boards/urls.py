from django.urls import path
from . import views

urlpatterns = [
    path("", views.board_list, name="home"),
    path("<str:slug>/", views.board_detail, name="detail"),
]
