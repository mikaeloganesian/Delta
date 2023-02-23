#On this page I'am initialising the createMenu function
from tkinter import *
from pagesArray import planymetryPageMain, stereometryPageMain

def exit(root):
    root.destroy()
    print('The app was closed')


def createMenu(root):
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

# Меню для планиметрии
    planemetryMenu = Menu(mainmenu, tearoff=0)
    planemetryMenu.add_command(
        label='Основы', command=lambda: planymetryPageMain.createPage())
    planemetryMenu.add_separator()
    planemetryMenu.add_command(label='Квадрат')
    planemetryMenu.add_command(label='Прямоугольник')
    planemetryMenu.add_command(label='Треугольник')
    planemetryMenu.add_command(label='Пр. треугольник')
    planemetryMenu.add_command(label='Окружность')
    planemetryMenu.add_command(label='Параллелограмм')
    planemetryMenu.add_command(label='Ромб')
    planemetryMenu.add_command(label='Трапеция')
# Меню для планеметрии

# Меню для стереометрии
    stereometryMenu = Menu(mainmenu, tearoff=0)
    stereometryMenu.add_command(
        label='Основы', command=lambda: stereometryPageMain.createPage())
    stereometryMenu.add_separator()
    stereometryMenu.add_command(label='Куб')
    stereometryMenu.add_command(label='Параллелепипед')
    stereometryMenu.add_command(label='Призмы')
    stereometryMenu.add_command(label='Цилиндр')
    stereometryMenu.add_command(label='Пирамиды')
    stereometryMenu.add_command(label='Конусы')
    stereometryMenu.add_command(label='Шар')
    stereometryMenu.add_command(label='Тетраэдр')
# Меню для стереометрии

# Меню для калькулятора
    calculatorMenu = Menu(mainmenu, tearoff=0)
    calculatorMenu.add_command(label='Планеметрический калькулятор')
    calculatorMenu.add_command(label='Стереометрический калькулятор')
# Меню для калькулятора

# Меню для справки
    infoMenu = Menu(mainmenu, tearoff=0)
    infoMenu.add_command(label='О проекте')
    infoMenu.add_separator()
    infoMenu.add_command(label='Создатели')
    infoMenu.add_command(label='Поддержка')
    infoMenu.add_command(label='Выход', command='exit')
# Меню для справки

    mainmenu.add_command(label='Главная')
    mainmenu.add_cascade(label='Планиметрия', menu=planemetryMenu)
    mainmenu.add_cascade(label='Стереометрия', menu=stereometryMenu)
    mainmenu.add_cascade(label='Калькуляторы', menu=calculatorMenu)
    mainmenu.add_cascade(label='Справка', menu=infoMenu)
