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


class Task_1:

    def __init__(self, window):
        self.Num_Trials = 5  # Кол-во испытаний
        self.Probability = 0.1  # Текущая вероятность
        # self.delta = 0.1  # Шаг изменения вероятности
        self.All_tables = []  # Результат всех вычислений
        self.window = window
        #self.window.grid_columnconfigure(0, weight=0)
        #self.window.grid_rowconfigure(0, weight=0)
        #self.window.grid_columnconfigure(1, weight=1)
        #self.window.grid_rowconfigure(1, weight=1)

        self.fr_left = Frame(window)
        #self.fr_left.configure(background='red')
        self.fr_left.grid(row=1, column=1)

        #self.fr_Sheet = Frame(window)
        #self.fr_Sheet.grid_columnconfigure(0, weight=1)
        #self.fr_Sheet.grid_rowconfigure(0, weight=1)
        #self.fr_Sheet.grid(row=0, column=0)
        #self.fr_Sheet.configure(background='black')
        #self.fr_Sheet.grid_propagate(False)

        self.fr_canvas = Frame(window)
        #self.fr_canvas.configure(background='red')
        self.fr_canvas.grid(row=0, column=1)

        self.F = Figure()
        self.canvas = FigureCanvasTkAgg(self.F, self.fr_canvas)
        self.canvas.draw()

        self.toolbar = CustomToolbar(self.canvas, self.fr_canvas)
        self.toolbar.update()
        self.toolbar.pack(side=BOTTOM, fill=X)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        self.Init_left_frame()

    def Init_left_frame(self):
        vcmd = (self.window.register(self.onValidate_num), '%d', '%s', '%S')
        vcmd1 = (self.window.register(self.onValidate_num_float), '%d', '%s', '%P')

        self.button_del = Button(self.fr_left, text="Произвести расчет", command=self.Perform_calc, anchor=W)
        self.button_del.configure(width=20, activebackground="#33B5E5")
        self.button_del.grid(row=0, column=0)

        self.Entry_N = Entry(self.fr_left, validate="key", validatecommand=vcmd, width=10, justify=LEFT)
        self.Entry_N.insert(0, str(self.Num_Trials))
        self.Entry_N.bind("<KeyRelease>", self.change_field_N)
        self.Entry_N.grid(row=1, column=1)

        self.label_N = Label(self.fr_left, text="Количество испытаний:")

        self.label_N.grid(row=1, column=0)

        self.label_P = Label(self.fr_left, text="Стартовая вероятность:")
        self.label_P.grid(row=2, column=0)

        self.entry_P = Entry(self.fr_left, validate="key", validatecommand=vcmd1, width=10, justify=LEFT)
        self.entry_P.grid(row=2, column=1)
        self.entry_P.insert(0, str(self.Probability))
        self.entry_P.bind("<KeyRelease>", self.change_field_P)

        self.label_table = Label(self.window, text="Вероятностная схема:")
        self.label_table.grid (row = 0, column = 0)



        #self.fr_left.pack(side=BOTTOM)

    def onValidate_num(self, d, s, S):
        # if it's deleting return True
        if d == "0":
            return True
        # Allow only digit, ":" and check the length of the string
        if ((not S.isdigit()) or len(s) >= 4):
            self.window.bell()
            return False
        return True

    def onValidate_num_float(self, d, s, P):
        if d == "0":
            return True
        try:
            float(P)
        except:
            self.window.bell()
            return False
        if float(P) > 1:
            self.window.bell()
            return False
        round(float(P), 3)
        return True

    def change_field_N(self, event):
        s = event.widget
        if len(s.get()) >= 1:
            self.Num_Trials = int(s.get())

    def change_field_P(self, event):
        s = event.widget
        if len(s.get()) >= 1:
            self.P = float(s.get())

    def Perform_calc(self):
        p_temp = self.Probability
        self.All_tables.clear()
        while p_temp <= 1:
            self.All_tables.append(Bernylli_Test(self.Num_Trials, p_temp))
            p_temp += 0.1
        Result_array = []
        for It in self.All_tables:
            Result_entropy = 0
            for It_inside in It:
                Result_entropy += (It_inside * math.log2(It_inside))
            Result_array.append(-1 * Result_entropy)

        Arr_ten_num = np.linspace(0,1,10)
        self.sheet = Sheet(self.window,data=[[f"{round(c,3)}"for c in Result_array] for r in range(1)],height=120, width=500,default_header = "numbers")
        self.sheet.enable_bindings()
        self.sheet.change_theme(theme="light blue")
        self.sheet.grid(row=1, column=0)
        self.F.clear()
        self.canvas.draw()
        a = self.F.add_subplot()
        a.set_title('Функция энтропии')
        a.plot(Arr_ten_num, Result_array)
        self.canvas.draw()
        self.toolbar.update()
        return

    def Draw_Bernylli_table(self,n):
        self.sheet = Sheet(self.window, data=[[f"{round(c, 3)}" for c in self.All_tables[n]] for r in range(1)],
                           height=120, width=900, default_header="numbers")
        self.sheet.enable_bindings()
        self.sheet.change_theme(theme="light blue")
        self.sheet.grid(row=0, column=0)

def Bernylli_Test(n, p):
    M = 0
    Result = []
    q = 1 - p
    while M <= n:
        Result.append(math.comb(n, M) * math.pow(p, M) * (math.pow(q, n - M)))
        M += 1
    return Result
