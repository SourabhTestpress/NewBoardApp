from django.urls import path
from . import views

urlpatterns = [
    path("", views.board_list, name="home"),
    path("all-topics/", views.topic_list, name="all_topics"),
    path("topic/<str:slug>", views.topic_detail, name="topic_detail"),
    path("<str:slug>/create-topic/", views.CreateTopicView.as_view(), name="new_topic"),
    path("<str:slug>/", views.board_detail, name="detail"),
]
