from tkinter import *
from testClass import page


planymetryPageMain = page('Основы', 'Планиметрия. Основы', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'images/planemetry/основы/slide-1.png')
stereometryPageMain = page('Основы', 'Стереометрия. Основы', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'images/planemetry/основы/slide-1.png')

def exit(root):
    root.destroy()
    print('The app was closed')



def createMenu(root):
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

# Меню для планиметрии
    planemetryMenu = Menu(mainmenu, tearoff=0)
    planemetryMenu.add_command(label='Основы', command= lambda: planymetryPageMain.createPage())
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
    stereometryMenu.add_command(label='Основы', command= lambda: stereometryPageMain.createPage())
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
