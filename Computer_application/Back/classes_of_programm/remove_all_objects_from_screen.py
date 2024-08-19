import sys

sys.path.append('')
from customtkinter import *


def destroy_all_from_screen(root, method: str) -> None:
    method = method.lower()
    list1 = []
    if method == 'pack':
        list1 = root.pack_slaves()
    elif method == 'grid':
        list1 = root.grid_slaves()
    elif method == 'place':
        list1 = root.slaves()
    for i in list1:
        i.destroy()
