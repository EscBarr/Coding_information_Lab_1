import Task1 as Base
import math
from tkinter import *
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


class Task_2(Base.Task_1):

    def __init__(self, window):
        self.Num_Trials = 0  # Кол-во испытаний
        self.Probability = float(0.1)  # Текущая вероятность
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

        self.label_P = Label(self.fr_left, text="Стартовая вероятность:")
        self.label_P.grid(row=2, column=0, padx=6, pady=6)

        self.entry_P = Entry(self.fr_left, validate="key", validatecommand=vcmd1, width=10, justify=LEFT)
        self.entry_P.grid(row=2, column=1, padx=6, pady=6)
        self.entry_P.insert(0, str(self.Probability))
        self.entry_P.bind("<KeyRelease>", self.change_field_P)

    def Perform_calc(self):
        p_temp = self.Probability
        self.All_tables.clear()
        while p_temp <= 1:
            self.All_tables.append(Calc_N(self.Num_Trials, p_temp)) #добавляем в итоговый массив с результатами N для каждой вероятности
            p_temp += 0.1
        Result_array = []
        for It in self.All_tables:#Считаем энтропию
            Result_entropy = 0
            for It_inside in It:
                Result_entropy += (It_inside * math.log2(It_inside))
            Result_array.append(-1 * Result_entropy)
        Result_array.insert(0, 0)
        self.draw_bernylli_table_task1(Result_array)
        return

def Calc_N(n, p):#ищем значение N при котором событие произойдет с вероятностью близкой к 1
    M = 0
    Result = []
    q = 1 - p
    Res_sum = 0
    Res = 0
    while Res_sum < 0.99:
        Res = p * math.pow(q, M)
        Res_sum += Res
        Result.append(Res)
        M += 1
    return Result
