import urllib.request
import orjson
from django.conf import settings
from django.core import cache


def get_boards():
    url = settings.FOURCHAN_BASE_URL + '/boards.json'
    resp = urllib.request.urlopen(url)
    resp_dict = orjson.loads(resp.read())
    boards = resp_dict.get('boards', {})
    board_list = [b.get('board') for b in boards if 'board' in b.keys()]
    if settings.LURKCHAN_ENABLE_CACHE:
        pass
    return board_list