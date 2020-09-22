from django.shortcuts import render
from django.http import HttpResponse

#  Imports from this folder
from .models import Board,Topic


def board_list(request):
    boards = Board.objects.all()
    context = {'boards':boards}
    return render(request,'boards/board_list.html',context)


def board_details(request,slug):
    return HttpResponse('Yet to be Implemented')


def topic_list(request):
    topics = Topic.objects.all()
    context = {'topics':topics}
    return render(request,'board_app/topic_list.html',context)


def topic_details(request,slug):
    return HttpResponse('Yet to be Implemented')
