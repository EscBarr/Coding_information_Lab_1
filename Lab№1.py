from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from Task1 import Task_1
import os

def create_Visuals():
    #opt_menu.delete("Просмотреть теорию")
    opt_menu.delete("Просмотреть визуализацию-игру")
    opt_menu.delete("Просмотреть визуализацию в виде графика")
    opt_menu.delete("Выход")
    label2.configure(text="")
    root.geometry("1466x750")

    global temp
    temp = Task_1(root)
    opt_menu.add_command(label="Выход", command=delete_Visuals)


def create_Visuals_graph():
    #opt_menu.delete("Просмотреть теорию")
    opt_menu.delete("Просмотреть визуализацию-игру")
    opt_menu.delete("Просмотреть визуализацию в виде графика")
    opt_menu.delete("Выход")
    label2.configure(text="")
    root.geometry("720x800")

    global temp

    opt_menu.add_command(label="Выход", command=delete_Visuals)

def Task1():

    label2.configure(text="")
    root.geometry("1466x750")
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
    # root.geometry("360x250")
    root.geometry("720x500")
    poetry = "«Моделирование процесса движения тела,\nброшенного под углом к горизонту»\n\nВыполнил студент гр. ДИПРБ 21\n              Ягафаров Тимур"
    label2 = Label(font=("Times", 14), text=poetry, justify=LEFT)
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