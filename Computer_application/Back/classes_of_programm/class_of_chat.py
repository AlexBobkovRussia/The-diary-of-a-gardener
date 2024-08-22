import sys

sys.path.append('')
from customtkinter import *
from Computer_application.Back.Computer_app.about_computer.size_of_screen import know_the_size_of_screen as sizes
from CTkListbox import *
from Computer_application.Back.chat.user import user


def send_messages(event):
    global text
    message = text.get('0.0', END)
    user(message)
    text.delete('0.0', END)


root = CTk()
h = sizes()['height'] - 70
h2 = int(str(h)[:])
w = sizes()['width'] + 1
print(w)
root.geometry(f'{w}x{h}+{-10}+0)')
root.resizable(0, 0)

listbox = CTkListbox(root)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

text = CTkTextbox(master=root, font=('Arial', 20), bg_color='black', fg_color='white', height=70, width=(w - 131),
                  border_color='black', border_width=2)
text.event_add('<<Paste>>', '<Control-igrave>')
text.event_add("<<Copy>>", "<Control-ntilde>")
# text.bind("<Control-Return>", command=lambda a: text.insert(END, '\n'))
text.bind("<Return>", command=lambda event: send_messages(event))
text.pack(side=LEFT, anchor=CENTER, padx=(10, 10), pady=(0, 10))
btn_send = CTkButton(master=root, text='➤', fg_color='#3399FF', text_color='white', font=('Arial', 30), height=50,
                     width=20, corner_radius=1000, command=lambda: (send_messages(a := 5),
                                                                    text.delete('1.0', END)))
btn_send.pack(side=RIGHT, anchor=SE, padx=(10, 20), pady=(0, 10))

listbox.insert(0, "Option 0")
listbox.insert("END", "Option 8")

root.mainloop()
