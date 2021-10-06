from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from Task1 import Task_1
from Task2 import Task_2
from Task3 import Task_3
import os

def create_Visuals():
    #opt_menu.delete("Просмотреть теорию")
    opt_menu.delete("Задача №1")
    opt_menu.delete("Задача №2")
    opt_menu.delete("Задача №3")
    opt_menu.delete("Выход")
    global label2
    label2.configure(text="")
    root.geometry("1173x720")

    global temp
    temp = Task_2(root)
    opt_menu.add_command(label="Выход", command=delete_Visuals)


def create_Visuals_graph():
    #opt_menu.delete("Просмотреть теорию")
    opt_menu.delete("Задача №1")
    opt_menu.delete("Задача №2")
    opt_menu.delete("Задача №3")
    opt_menu.delete("Выход")
    global label2
    label2.configure(text="")
    root.geometry("1173x720")

    global temp
    temp = Task_3(root)
    opt_menu.add_command(label="Выход", command=delete_Visuals)

def Task1():
    opt_menu.delete("Задача №1")
    opt_menu.delete("Задача №2")
    opt_menu.delete("Задача №3")
    opt_menu.delete("Выход")
    global label2
    label2.configure(text="")
    root.geometry("1173x720")
    global temp
    temp = Task_1(root)
    opt_menu.add_command(label="Выход", command=delete_Visuals)

def delete_Visuals():
    temp.__del__()
    opt_menu.delete("Выход")
    opt_menu.delete(0)
    opt_menu.add_command(label="Задача №1", command=Task1)
    opt_menu.add_command(label="Задача №2", command=create_Visuals)
    opt_menu.add_command(label="Задача №3", command=create_Visuals_graph)
    opt_menu.add_separator()
    opt_menu.add_command(label="Выход", command=root.destroy)
    root.geometry("720x500")
    poetry = "Лабораторная работа №1.\n  «Энтропия. Свойства энтропии»\n\nВыполнил студент гр. ДИПРБ 31\nЯгафаров Тимур"
    global label2
    label2.configure(text=poetry)
    label2.place(relx=.3, rely=.4)


global root
root = Tk()
#root.configure(background='grey80')
root.tk_setPalette(background='grey80', foreground='Black',
                   activeBackground='Black', activeForeground='grey80')
root.title("Лабораторная работа №1. «Энтропия. Свойства энтропии»")
# root.geometry("360x250")
root.geometry("720x500")
# Creating a Font object of "TkDefaultFont"
defaultFont = font.nametofont("TkDefaultFont")
# Overriding default-font with custom settings
# i.e changing font-family, size and weight
defaultFont.configure(family="Times", size=12)
global opt_menu
opt_menu = Menu(font=("Times", 14), tearoff=0)
opt_menu.add_command(label="Задача №1", command = Task1)
opt_menu.add_command(label="Задача №2", command=create_Visuals)
opt_menu.add_command(label="Задача №3", command=create_Visuals_graph)
opt_menu.add_separator()
opt_menu.add_command(label="Выход", command=root.destroy)
main_menu = Menu()
main_menu.add_cascade(label="Меню", menu=opt_menu)
#main_menu.add_cascade(label="О программе")

poetry = "Лабораторная работа №1.\n  «Энтропия. Свойства энтропии»\n\nВыполнил студент гр. ДИПРБ 31\nЯгафаров Тимур"
global label2
label2 = Label(font=("Times", 14), text=poetry, justify=CENTER)
label2.place(relx=.3, rely=.4)
root.config(menu=main_menu)

root.mainloop()