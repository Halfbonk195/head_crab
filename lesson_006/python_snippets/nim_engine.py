from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}
_sorted_keys = None

def put_stones():
    """ расположить камни на игровой поверхности """
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHES_SIZE)
    _sorted_keys = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    step_successed = False
    if position in _holder:
        if 0 < quantity <= _holder[position]:
            _holder[position] -= quantity
            step_successed = True

    return step_successed



def get_bunches():
    res = []
    for key in _sorted_keys:
        res.append(_holder[key])
    return res


def is_gameover():
    return sum(_holder.values()) == 0
