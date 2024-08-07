import sys

sys.path.append('')
from Computer_application.to_sort.Computer_app.analysing.data_analyse import check_on_right_date
import os
from string import ascii_lowercase
import re


def is_every_email_letter_is_latin(email):
    a = ascii_lowercase
    counter, counter2 = 0, 0
    for i in email:
        if i.isalpha() and i in a:
            counter += 1
        counter2 += 1
    if counter == counter2:
        return True
    return False


def is_right_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    return False


def is_right_phone_number(phone_number):
    # Саму библиотеку не знаю, а также регурялные выражения выше -> взял из Интернета
    import phonenumbers
    from phonenumbers import carrier
    from phonenumbers.phonenumberutil import number_type
    number = phone_number
    try:
        if carrier._is_mobile(number_type(phonenumbers.parse(number))):
            return True
    except:
        return False


def is_right_registration(first_name, second_name, third_name, date, email, login, password1, password2, phone):
    global to_change
    counter = 1

    if first_name.isalpha() and second_name.isalpha() and third_name.isalpha():
        counter += 3

    if check_on_right_date(date):
        counter += 1
    else:
        to_change += 'ввести правильную дату формата DD.MM.YYYY (ДД.ММ.ГГГГ)'

    if email:
        counter += 1
    else:
        to_change += 'ввести правильный email'

    if password1 == password2:
        counter += 2
    else:
        to_change += 'ввести одинаковые пароли'

    if is_right_phone_number(phone):
        counter += 1
    else:
        to_change += 'ввести правильный номер телефона'

    if counter == 9:
        if not os.path.exists('Data_of_user.txt'):
            file = open('Data_of_user.txt', 'w', encoding='utf-8')
            file.close()
        file = open('Data_of_user.txt', 'r+', encoding='utf-8')
        lines = file.readlines()
        file.close()
        if len(lines) > 0:
            file = open('Data_of_user.txt', 'w', encoding='utf-8')
            file.close()
        file = open('Data_of_user.txt', 'r+', encoding='utf-8')
        file.write(f'Имя пользователя: {first_name}\n')
        file.write(f'Фамилия пользователя: {second_name}\n')
        file.write(f'Отчество пользователя: {third_name}\n')
        file.write(f'Дата рождения пользователя: {date}\n')
        file.write(f'email пользователя: {email}\n')
        file.write(f'login пользователя: {login}\n')
        file.write(f'пароль пользователя: {password1}\n')
        file.write(f'телефон пользователя: {phone}')
        file.close()
        return True
    return False, to_change


to_change = 'Надо исправить: '

if __name__ == '__main__':
    assert is_right_registration('Алексей', 'Бобков', 'Владимирович', '16.02.2011', 'bobkovalex.yaundex.ru@yandex.ru',
                                 'login', 'asdfvcxz16022011', 'asdfvcxz16022011', '+7 920 067 52 23') == True
