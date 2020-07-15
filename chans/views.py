from django.shortcuts import render
from django.http import HttpResponse
from .fourchan.utils import get_boards
# Create your views here.


def boards(request, chan_name: str):
    board_list = get_boards()
    return render(request,
                  'fourchan/fourchan_boards.html',
                  context={'chan_name': chan_name, 'board_list': board_list})



def category(request, chan_name: str, board: str, page=1):
    return HttpResponse(chan_name + str(page))


def thread(request, chan_name: str, board:str, thread: str):
    return HttpResponse(chan_name+board+thread)