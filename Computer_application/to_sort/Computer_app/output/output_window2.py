from tkinter import Tk, Label, Button, Entry
import os

window = Tk()

window.geometry('1268x833+1+70')
window.resizable(False, False)
window.title('Дневник семян')
window.config(bg='green')

file_settings = open('settings.txt', 'r', encoding='utf-8')
f = file_settings.readlines()
file_settings.close()
counter = 1
lbl3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')


def list_page():
    global counter
    global entr1
    global entr2
    global lbl3
    if counter == 1:
        counter_1 = 0
        if len(entr0.get()) == 0 and counter_1 == 0:
            counter_1 = 1
            lbl3.grid(row=2, column=0, padx=(480, 10), pady=(50, 0))
        else:
            if counter_1 == 1:
                lbl3.destroy()
                lbl3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
        if counter_1 == 0:
            list1 = [entr0.get()]
            lbl0.destroy()
            entr0.destroy()
            lbl1 = Label(window, text='Введите ваш пароль:', font='Arial 20', bg='green', fg='white')
            entr1 = Entry(window, font='Arial 20', bg='white', fg='black')
            lbl1.grid(row=0, column=0, padx=(480, 10), pady=(200, 0))
            entr1.grid(row=0, column=0, padx=(480, 10), pady=(280, 0))

            lbl2 = Label(window, text='Повторите ваш пароль:', font='Arial 20', bg='green', fg='white')
            entr2 = Entry(window, font='Arial 20', bg='white', fg='black')
            lbl2.grid(row=1, column=0, padx=(480, 10), pady=(100, 0))
            entr2.grid(row=1, column=0, padx=(480, 10), pady=(180, 0))
            counter += 1
    if counter == 2:
        entr1 = entr1.get()
        entr2 = entr2.get()
        if entr1 != entr2:
            lbl3 = Label(window, text='Пароли не совпадают', font='Arial 20', bg='red', fg='white')
            lbl3.grid(row=2, column=0, padx=(480, 10), pady=(50, 0))
        elif len(entr1) == 0 or len(entr2) == 0:
            lbl3 = Label(window, text='Заполните все поля', font='Arial 20', bg='red', fg='white')
            lbl3.grid(row=2, column=0, padx=(480, 10), pady=(50, 0))
        else:
            pass
    if counter == 3:
        pass
    if counter == 4:
        pass


def start_presentation():
    def open_powerpoint_presentation(file_path):
        os.system(f"start powerpnt {file_path}")

    file_path = "C:/Users/user/PycharmProjects/book_of_plants2/Презентация_проекта_book_of_plants_(Дневник_семян).pptx"
    open_powerpoint_presentation(file_path)


if len(f) == 0:
    file_settings = open('settings.txt', 'r+', encoding='utf-8')

    lbl0 = Label(window, text='Введите ваш логин:', font='Arial 20', bg='green', fg='white')
    lbl0.grid(row=0, column=0, padx=(480, 10), pady=(300, 0))
    entr0 = Entry(window, font='Arial 20', bg='white', fg='black')
    entr0.grid(row=1, column=0, padx=(480, 10), pady=(10, 0))
    # btn0 = Button(window, text='Отправить', font='Arial 20', command=is_right_registration)
    # btn0.grid(row=2, column=0, padx=480, pady=(300, 0))
    btn0 = Button(window, text='Далее', font='Arial 30', command=list_page)
    btn0.grid(row=3, column=1)

    # lbl1 = Label(window, text='Введите ваш пароль:', font='Arial 20', bg='green', fg='white')
    # lbl1.grid(row=0, column=1)
    # entr1 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr1.grid(row=1, column=1, padx=7)
    #
    # lbl2 = Label(window, text='Введите ваш логин:', font='Arial 20', bg='green', fg='white')
    # lbl2.grid(row=0, column=2)
    # entr2 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr2.grid(row=1, column=2, padx=7)
    #
    # lbl3 = Label(window, text='Введите ваш логин:', font='Arial 20', bg='green', fg='white')
    # lbl3.grid(row=0, column=3)
    # entr3 = Entry(window, font='Arial 20', bg='white', fg='black')
    # entr3.grid(row=1, column=3, padx=7)
    file_settings.close()


def to_bind(event):
    list_page()


window.bind('<Return>', to_bind)

window.mainloop()
