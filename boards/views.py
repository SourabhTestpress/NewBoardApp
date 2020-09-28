from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import Board, Topic


def board_list(request):
    boards = Board.objects.all()
    context = {"boards": boards}
    return render(request, "boards/list.html", context)


def board_detail(request, slug):
    return HttpResponse("Yet to be Implemented")


def topic_list(request):
    topics = Topic.objects.all()
    context = {"topics": topics}
    return render(request, "boards/topic_list.html", context)


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    context = {"topic": topic}
    return render(request, "boards/topic_detail.html", context)
