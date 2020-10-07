from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from boards.models import Board, Topic, Post
from boards.forms import CreateTopicForm


def board_list(request):
    boards = Board.objects.all()
    context = {"boards": boards}
    return render(request, "boards/list.html", context)


def board_detail(request, slug):
    board = get_object_or_404(Board, slug=slug)
    context = {"board": board}
    return render(request, "boards/detail.html", context)


def topic_list(request):
    topics = Topic.objects.all()
    context = {"topics": topics}
    return render(request, "topic/list.html", context)


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    context = {"topic": topic}
    return render(request, "topic/detail.html", context)


class CreateTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    form_class = CreateTopicForm
    template_name = "topic/new_topic.html"

    def get_success_url(self):
        return reverse("detail", args=(self.kwargs.get("slug"),))

    def form_valid(self, form):
        saved_form_object = form.save(current_user=self.request.user)
        return super().form_valid(saved_form_object)

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        initial["board"] = get_object_or_404(Board, slug=self.kwargs.get("slug"))
        return initial
