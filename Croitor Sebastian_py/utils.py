def clear_file(filename):
    with open(filename, 'w'):
        pass


def my_sorted(iterable, *, key=lambda x: x, reverse=False):
    n = len(iterable)
    if reverse is True:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key(iterable[j]) < key(iterable[j + 1]):
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    else:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key(iterable[j]) > key(iterable[j + 1]):
                    iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    return iterable
