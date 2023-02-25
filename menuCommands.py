# On this page I'am initialising the createMenu function
from tkinter import *
from pagesArray import pagesArray
from aboutProjectPage import createAboutProjectPage


def exit(root):
    root.destroy()
    print('The app was closed')


def createMenu(root):
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

# Меню для планиметрии
    planemetryMenu = Menu(mainmenu, tearoff=0)
    planemetryMenu.add_command(
        label='Основы', command=lambda: pagesArray[0].createPage())
    planemetryMenu.add_separator()
    planemetryMenu.add_command(
        label='Квадрат', command=lambda: pagesArray[1].createPage())
    planemetryMenu.add_command(
        label='Прямоугольник', command=lambda: pagesArray[2].createPage())
    planemetryMenu.add_command(
        label='Треугольник', command=lambda: pagesArray[3].createPage())
    planemetryMenu.add_command(
        label='Пр. треугольник', command=lambda: pagesArray[4].createPage())
    planemetryMenu.add_command(
        label='Окружность', command=lambda: pagesArray[5].createPage())
    planemetryMenu.add_command(
        label='Параллелограмм', command=lambda: pagesArray[6].createPage())
    planemetryMenu.add_command(
        label='Ромб', command=lambda: pagesArray[7].createPage())
    planemetryMenu.add_command(
        label='Трапеция', command=lambda: pagesArray[8].createPage())
# Меню для планеметрии

# Меню для стереометрии
    stereometryMenu = Menu(mainmenu, tearoff=0)
    stereometryMenu.add_command(
        label='Основы', command=lambda: pagesArray[9].createPage())
    stereometryMenu.add_separator()
    stereometryMenu.add_command(
        label='Куб', command=lambda: pagesArray[10].createPage())
    stereometryMenu.add_command(
        label='Параллелепипед', command=lambda: pagesArray[11].createPage())
    stereometryMenu.add_command(
        label='Призмы', command=lambda: pagesArray[12].createPage())
    stereometryMenu.add_command(
        label='Цилиндр', command=lambda: pagesArray[13].createPage())
    stereometryMenu.add_command(
        label='Пирамиды', command=lambda: pagesArray[14].createPage())
    stereometryMenu.add_command(
        label='Конусы', command=lambda: pagesArray[15].createPage())
    stereometryMenu.add_command(
        label='Шар', command=lambda: pagesArray[16].createPage())
    stereometryMenu.add_command(
        label='Тетраэдр', command=lambda: pagesArray[17].createPage())
# Меню для стереометрии

# Меню для калькулятора
    calculatorMenu = Menu(mainmenu, tearoff=0)
    calculatorMenu.add_command(label='Планеметрический калькулятор')
    calculatorMenu.add_command(label='Стереометрический калькулятор')
# Меню для калькулятора

# Меню для справки
    infoMenu = Menu(mainmenu, tearoff=0)
    infoMenu.add_command(
        label='О проекте', command=lambda: createAboutProjectPage())
    infoMenu.add_separator()
    infoMenu.add_command(label='Created by 15lu.akari')
    infoMenu.add_command(label='4276 4000 7852 9352')
    infoMenu.add_separator()
    infoMenu.add_command(label='Выход', command='exit')
# Меню для справки

    mainmenu.add_cascade(label='Планиметрия', menu=planemetryMenu)
    mainmenu.add_cascade(label='Стереометрия', menu=stereometryMenu)
    mainmenu.add_cascade(label='Калькуляторы', menu=calculatorMenu)
    mainmenu.add_cascade(label='Справка', menu=infoMenu)
