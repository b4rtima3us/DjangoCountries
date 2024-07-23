from itertools import chain


def flatten_list(item: list):
    return list(chain.from_iterable(item))
