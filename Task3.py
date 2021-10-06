import Task1 as Base
import math
from tkinter import *
import numpy as np
import scipy.integrate as integrate
import matplotlib
from tksheet import Sheet

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class CustomToolbar(NavigationToolbar2Tk):
    def __init__(self, canvas_, parent_):
        self.toolitems = (
            ('Home', 'Вернуть исходный вид', 'home', 'home'),
            ('Back', 'Назад к предыдущему виду', 'back', 'back'),
            ('Forward', 'Вперед к следующему виду', 'forward', 'forward'),
            (None, None, None, None),
            ('Pan', 'Перемещение по осям левой мышью, масштабирование осей правой', 'move', 'pan'),
            ('Zoom', 'Выделение области для приближения', 'zoom_to_rect', 'zoom'),
            (None, None, None, None),
            ('Save', 'Сохранить рисунок', 'filesave', 'save_figure'),
        )
        NavigationToolbar2Tk.__init__(self, canvas_, parent_)


class Task_3(Base.Task_1):

    def __init__(self, window):
        self.Num_Trials = 10  # Кол-во изделий
        self.Num_M = 3  # Выборка

        self.All_tables = []  # Результат всех вычислений
        self.window = window

        self.fr_left = Frame(window)
        self.fr_left.grid(row=1, column=0, padx=6, pady=6)

        self.fr_Sheet = Frame(window)
        self.fr_Sheet.grid(row=0, column=1, padx=6, pady=6)

        self.fr_List_of_tables = Frame(window)
        self.fr_List_of_tables.grid(row=1, column=1, padx=6, pady=6)

        self.fr_canvas = Frame(window)
        self.fr_canvas.grid(row=0, column=0, padx=6, pady=6)

        self.F = Figure()
        self.canvas = FigureCanvasTkAgg(self.F, self.fr_canvas)
        self.canvas.draw()

        self.toolbar = CustomToolbar(self.canvas, self.fr_canvas)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        self.Init_left_frame()

    def Init_left_frame(self):
        vcmd = (self.window.register(self.onValidate_num), '%d', '%s', '%S')
        vcmd1 = (self.window.register(self.onValidate_num_float), '%d', '%s', '%P')

        self.button_del = Button(self.fr_left, text="Произвести расчет", command=self.Perform_calc, anchor=W)
        self.button_del.configure(width=15, activebackground="#33B5E5")
        self.button_del.grid(row=0, column=0, padx=6, pady=6)

        self.Entry_N = Entry(self.fr_left, validate="key", validatecommand=vcmd, width=10, justify=LEFT)
        self.Entry_N.insert(0, str(self.Num_Trials))
        self.Entry_N.bind("<KeyRelease>", self.change_field_N)
        self.Entry_N.grid(row=1, column=1, padx=6, pady=6)

        self.label_N = Label(self.fr_left, text="Количество Деталей:")

        self.label_N.grid(row=1, column=0, padx=6, pady=6)

        self.Entry_M = Entry(self.fr_left, validate="key", validatecommand=vcmd, width=10, justify=LEFT)
        self.Entry_M.insert(0, str(self.Num_M))
        self.Entry_M.bind("<KeyRelease>", self.change_field_M)
        self.Entry_M.grid(row=2, column=1, padx=6, pady=6)

        self.label_N = Label(self.fr_left, text="Значение выборки:")

        self.label_N.grid(row=2, column=0, padx=6, pady=6)


    def Perform_calc(self):
        self.All_tables.clear()
        Temp_K = 0
        while Temp_K <= self.Num_Trials:
            self.All_tables.append(Calc_N(self.Num_Trials, self.Num_M, Temp_K))
            Temp_K += 1

        Result_array = []
        for It in self.All_tables:
            Result_entropy = 0
            for It_inside in It:
                Result_entropy += (It_inside * math.log2(It_inside))
            Result_array.append(-1 * Result_entropy)
        #Result_array.insert(0, 0)
        self.draw_bernylli_table_task1(Result_array)
        return

    def change_field_M(self, event):
        s = event.widget
        if len(s.get()) >= 1:
            self.Num_M = int(s.get())


def Calc_N(n, m, k):
    i = 0
    Result = []
    Res = 0
    while i <= m and i <= k:
        if ((n - k) < (m - i)):
            break
        Res = math.comb(k, i) * math.comb(n - k, m - i) / math.comb(n, m)
        Result.append(Res)
        i += 1
    return Result
