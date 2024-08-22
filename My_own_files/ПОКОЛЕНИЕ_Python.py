from time import time
def square(n: int) -> int:
    return n ** 2


def calculate_sum(n: int) -> int:
    start = time()
    if n == 1:
        return 1
    counter = 1
    counter += sum(map(square, range(3, n + 1, 2)))
    if n % 2 == 0:
        counter -= sum(map(square, range(2, n + 1, 2)))
    else:
        counter -= sum(map(square, range(2, n, 2)))
    all_time = time() - start
    if all_time <= 2:
        return counter
    else:
        return 'Время вышло'

assert calculate_sum(1) == 1
assert calculate_sum(4) == -10
assert calculate_sum(5) == 15