import sys

sys.path.append('')
from tkinter import Tk, Label, Button, Entry, END
from Computer_application.Back.generate_passwords import generate_password
import os

# from Computer_app.the_screensaver.start import root

window = Tk()

window.geometry('1268x750+1+20')
window.resizable(False, False)
window.title('Дневник семян')
window.config(bg='green')

if not os.path.exists('settings.txt'):
    file = open('settings.txt', 'w', encoding='utf-8')
    file.close()
file_settings = open('settings.txt', 'r', encoding='utf-8')
f = file_settings.readlines()
file_settings.close()
counter = 1
# 0 = NO
# 1 = YES
which_number_for_constants_for_login_will_be = 0
which_number_for_constants_for_password_will_be = -1
was_it_place_or_not_for_password = {'lbl_error_2': False, 'lbl_error_3': False}
dict_of_data = {}


def clean_all_fields(*args):
    for i in args:
        i.delete(0, END)


def write_in_txt_file(what_write: dict, *, name: str, encod: str, format: str, separator: str = ':',
                      end: str = '\n') -> None:
    if len(what_write) > 0:
        if not os.path.exists(name):
            file = open(name, 'w+', encoding=encod)
            file.close()
        file = open(name, format, encoding=encod)
        for i in what_write.keys():
            file.write(f'{i} {separator} {what_write[i]}{end}')


# def list_page():
# global dict_of_data
# global counter
# global entr1
# global entr2
# global lbl1
# global lbl2
# global btn1
# global btn2
# global lbl_error_1
# global lbl_error_2
# global lbl_error_3
# global which_number_for_constants_for_login_will_be
# global which_number_for_constants_for_password_will_be
# global was_it_place_or_not_for_password
# if counter == 1:
#     if which_number_for_constants_for_login_will_be == 0:
#         # 0 -> NO
#         # 1 -> YES and if it was placed -> destroy
#         need_place_error_or_not = 0
#     else:
#         # 0 -> NO
#         # 1 -> YES and if it was placed -> destroy
#         need_place_error_or_not = 1
#     login = entr0.get().strip()
#     if len(login) == 0 and need_place_error_or_not == 0:
#         need_place_error_or_not = 1
#         lbl_error_1 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
#         lbl_error_1.place(x=500, y=500)
#         print('FIRST IF IS DID')
#         which_number_for_constants_for_login_will_be = 1
#     if need_place_error_or_not == 1 and len(login) != 0:
#         lbl_error_1.destroy()
#         need_place_error_or_not = 0
#         which_number_for_constants_for_login_will_be = 0
#         print('SECOND IF IS DID')
#     if need_place_error_or_not == 0:
#         dict_of_data['login'] = login
#         # lbl3.destroy()
#         lbl0.destroy()
#         entr0.destroy()
#         lbl1 = Label(window, text='Придумайте пароль:', font='Arial 20', bg='green', fg='white')
#         entr1 = Entry(window, font='Arial 20', bg='white', fg='black')
#         lbl1.place(x=510, y=200)
#         entr1.place(x=490, y=250)

#         lbl2 = Label(window, text='Повторите пароль:', font='Arial 20', bg='green', fg='white')
#         entr2 = Entry(window, font='Arial 20', bg='white', fg='black')
#         lbl2.place(x=520, y=400)
#         entr2.place(x=490, y=450)

#         btn1 = Button(window, text='Сгенерировать безопасный пароль', font='Arial 20', command=insert_safe_password)
#         btn1.place(x=410, y=520)

#         btn2 = Button(window, text='Очистить все поля', font='Arial 20', command=lambda: clean_all_fields(entr1, entr2))
#         btn2.place(x=500, y=590)
#         counter += 1
#         print(dict_of_data)
#         del which_number_for_constants_for_login_will_be
# if counter == 2:
#     password1 = entr1.get()
#     password2 = entr2.get()
#     if which_number_for_constants_for_password_will_be != -1:
#         if password1 != password2:
#             lbl_error_2 = Label(window, text='Пароли не совпадают', font='Arial 20', bg='red', fg='white')
#             lbl_error_2.place(x=500, y=660)
#             was_it_place_or_not_for_password['lbl_error_2'] = True
#             if was_it_place_or_not_for_password['lbl_error_3']:
#                 exec(f'lbl_error_3.destroy()')
#                 was_it_place_or_not_for_password['lbl_error_3'] = False
#         elif (len(password1) == 0 or len(password2) == 0) and (password1 == '' and password2 == ''):
#             lbl_error_3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
#             lbl_error_3.place(x=500, y=660)
#             was_it_place_or_not_for_password['lbl_error_3'] = True
#             if was_it_place_or_not_for_password['lbl_error_2']:
#                 exec(f'lbl_error_2.destroy()')
#                 was_it_place_or_not_for_password['lbl_error_2'] = False
#         else:
#             dict_of_data['password'] = password1
#             lbl1.destroy()
#             entr1.destroy()
#             lbl2.destroy()
#             entr2.destroy()
#             btn1.destroy()
#             btn2.destroy()
#             if was_it_place_or_not_for_password['lbl_error_2']:
#                 exec(f'lbl_error_2.destroy()')
#                 was_it_place_or_not_for_password['lbl_error_2'] = False
#             if was_it_place_or_not_for_password['lbl_error_3']:
#                 exec(f'lbl_error_3.destroy()')
#                 was_it_place_or_not_for_password['lbl_error_3'] = False
#             print(dict_of_data)
#             counter += 1
#     else:
#         which_number_for_constants_for_password_will_be = 0
# if counter == 3:
#     counter += 1
# if counter == 4:
#     counter += 1
#     write_in_txt_file(dict_of_data, name='settings.txt', encod='utf-8', format='w')


def start_presentation():
    def open_powerpoint_presentation(file_path):
        os.system(f"start powerpnt {file_path}")

    file_path = "C:/Users/user/PycharmProjects/book_of_plants2/Презентация_проекта_book_of_plants_(Дневник_семян).pptx"
    open_powerpoint_presentation(file_path)


def insert_safe_password():
    global entr1
    a = generate_password()
    entr1.delete(0, END)
    entr1.insert(0, a)


def sign_in(username, password):
    global entr0
    global entr1
    global lbl0
    global lbl1
    global btn2
    global btn3
    file_settings = open('settings.txt', 'r+', encoding='utf-8')

    file_settings.write(f'username: {username}\n')
    file_settings.write(f'password: {password}')
    file_settings.close()


if len(f) == 0:
    lbl0 = Label(window, text='Username or Email', font='Arial 20', bg='green', fg='white')
    lbl0.place(x=510, y=150)
    # lbl0.grid(row=0, column=0, )
    # lbl0.pack(anchor='center')
    entr0 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr0.place(x=480, y=200)
    # btn0 = Button(window, text='Отправить', font='Arial 20', command=is_right_registration)
    # btn0.grid(row=2, column=0, padx=480, pady=(300, 0))
    lbl1 = Label(window, text='Password', font='Arial 20', bg='green', fg='white')
    # lbl1.place(x=560, y=300)
    entr1 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr1.place(x=480, y=350)

    btn2 = Button(window, text='Generate a secure password', font='Arial 20', command=insert_safe_password)
    # btn2.place(x=440, y=450)

    btn3 = Button(window, text='Sign in', font='Arial 20', command=lambda: sign_in(entr0.get(), entr1.get()))


    # btn3.place(x=570, y=580)

    def to_bind2(event):
        sign_in(entr0.get(), entr1.get())


    window.bind('<Return>', to_bind2)

elif len(f) == 2:
    pass

# root.mainloop()
window.mainloop()
