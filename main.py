from tkinter import *
from tkinter import ttk

categoryName = ['Квадрат', 'Прямоугольник', 'Треугольник', 'Пр. треугольник', 'Круг', 'Параллелограмм', 'Ромб', 'Трапеция', 'Сфера']

def finish():
    root.destroy()
    print('Закрытие приложения')

# window settings
root = Tk()
root.title('Delta - шпаргалка по геометрии')
root.state('zoomed')
root.protocol('WM_DELETE_WINDOW', finish)

# UI inicializating

i = 0
for r in range(3):
    for c in range(3):
        category = ttk.Button(text=categoryName[i], width='50', padding='10')
        category.grid(row=r, column=c)
        i+=1

# open the window
root.mainloop()