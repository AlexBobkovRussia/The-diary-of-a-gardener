import sys

sys.path.append('')
from screeninfo import get_monitors


def know_the_size_of_screen() -> dict:
    '''Функция know_the_size_of_screen возвращает словарь, состоящий из трех элементов: 
    "name": Имя монитора
    "width": Ширину монитора
    "height": Высоту монитора'''
    for monitor in get_monitors():
        return {'name': monitor.name, 'width': monitor.width, 'height': monitor.height}
