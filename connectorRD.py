import os
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk

def exit():
    window.destroy()

def connectorssh():
    if combo.get() == "node1":
        window.quit()
        os.system("ssh имя_пользователя@ip_адрес")
        window.mainloop()
    elif combo.get() == "node2":
        window.quit()
        os.system("ssh имя_пользователя@ip_адрес")
        window.mainloop()
    elif combo.get() == "node3":
        window.quit()
        os.system("ssh имя_пользователя@ip_адрес")
        window.mainloop()
    elif combo.get() == "node4":
        window.quit()
        os.system("ssh имя_пользователя@ip_адрес")
        window.mainloop()
def connectorsftp():
    if combo.get() == "node1":
        window.quit()
        os.system("dolphin sftp://имя_пользователя@ip_адрес/")
        window.mainloop()
    elif combo.get() == "node2":
        window.quit()
        os.system("dolphin sftp://имя_пользователя@ip_адрес/")
        window.mainloop()
    elif combo.get() == "node3":
        window.quit()
        os.system("dolphin sftp://имя_пользователя@ip_адрес/")
        window.mainloop()
    elif combo.get() == "node4":
        window.quit()
        os.system("dolphin sftp://имя_пользователя@ip_адрес/")
        window.mainloop()


window = Tk()
window.title("SSH/SFTP Connector by RIVENDELL")
window.geometry('380x250')
lbl = Label(window, text="Пожалуйста выберите нужную ноду для подключения по SSH")
lbl.grid(column=0, row=0)
#combo = ttk.Combobox(window)
#combo = (window, vaules=["x173", "x204", "proxy", "backup"])
combo = ttk.Combobox(window, values=["node1", "node2", "node3", "node4"])
combo.current(0)  # установите вариант по умолчанию
combo.grid(column=0, row=2)
btn = Button(window, text="Подключиться по SSH", command=connectorssh)
btn.grid(column=0, row=4)
btn = Button(window, text="Подключиться по SFTP", command=connectorsftp)
btn.grid(column=0, row=8)
quit = Button(window, text="Выйти", command=exit)
quit.grid(column=0, row=14)
lbl = Label(window, text="Используйте exit или комбинацию клавиш CTRL+A+D\nдля отключения от сервера по SSH")
lbl.grid(column=0, row=6)
lbl2 = Label(window, text="Закройте файловый менеджер Dolphin для\nотключения от сервера по SFTP")
lbl2.grid(column=0, row=10)
info = Label(window, text="Использовать только в OC Linux с KDE или\nфайловым менеджером Dolphin")
info.grid(column=0, row=16)


window.mainloop()
