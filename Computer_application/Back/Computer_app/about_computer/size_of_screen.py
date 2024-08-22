import sys

sys.path.append('.')

from pyautogui import size


def know_the_size_of_screen() -> tuple[int, int]:
    return size()
