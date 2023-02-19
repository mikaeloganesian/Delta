from tkinter import *

def createMenu(root):
    mainmenu = Menu(root)   
    root.config(menu=mainmenu)              #прикрепили объект меню к root

#Меню для планеметрии
    planemetryMenu = Menu(mainmenu, tearoff=0)
    planemetryMenu.add_command(label='Основы')
    planemetryMenu.add_separator()
    planemetryMenu.add_command(label='Квадрат')
    planemetryMenu.add_command(label='Прямоугольник')
    planemetryMenu.add_command(label='Треугольник')
    planemetryMenu.add_command(label='Пр. треугольник')
    planemetryMenu.add_command(label='Окружность')
    planemetryMenu.add_command(label='Параллелограмм')
    planemetryMenu.add_command(label='Ромб')
    planemetryMenu.add_command(label='Трапеция')
#Меню для планеметрии

#Меню для стереометрии
    stereometryMenu = Menu(mainmenu, tearoff=0)
    stereometryMenu.add_command(label='Основы')
    stereometryMenu.add_separator()
    stereometryMenu.add_command(label='Куб')
    stereometryMenu.add_command(label='Параллелепипед')
    stereometryMenu.add_command(label='Призмы')
    stereometryMenu.add_command(label='Цилиндр')
    stereometryMenu.add_command(label='Пирамиды')
    stereometryMenu.add_command(label='Конусы')
    stereometryMenu.add_command(label='Шар')
    stereometryMenu.add_command(label='Тетраэдр')
#Меню для стереометрии
    
#Меню для стереометрии
    calculatorMenu = Menu(mainmenu, tearoff=0)
    calculatorMenu.add_command(label='Планеметрический калькулятор')
    calculatorMenu.add_command(label='Стереометрический калькулятор')
#Меню для стереометрии

    mainmenu.add_command(label='Главная')
    mainmenu.add_cascade(label='Планеметрия', menu=planemetryMenu)
    mainmenu.add_cascade(label='Стереометрия', menu=stereometryMenu)
    mainmenu.add_cascade(label='Калькуляторы', menu=calculatorMenu)
    mainmenu.add_command(label='Выход', command='exit')