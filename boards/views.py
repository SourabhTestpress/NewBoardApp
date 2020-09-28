from django.shortcuts import render
from django.http import HttpResponse


from .models import Board


def board_list(request):
    boards = Board.objects.all()
    context = {"boards": boards}
    return render(request, "boards/list.html", context)


def board_detail(request, slug):
    return HttpResponse("Yet to be Implemented")
