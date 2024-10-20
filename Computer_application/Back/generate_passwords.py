# Генератор безопасных паролей
from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
chars += digits
chars += lowercase_letters
chars += uppercase_letters
chars += punctuation


def generate_password():
    global chars
    q = ''
    for i in range(15):
        c = choice(chars)
        if c not in q:
            q += c
    return q


if __name__ == '__main__':
    generate_password()