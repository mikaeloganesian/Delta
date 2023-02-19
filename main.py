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

# UI creating
helloLabel = Label(root, text='Hello User, this is Delta', font=('Arial', '20', 'bold'), width=20, pady=8)

planemetryFrame = Frame(root, borderwidth=3, relief=SOLID)
planemetryLabel = Label(planemetryFrame, text='Планеметрия', font=('Arial', '14', 'bold'), width=50, height=15, anchor='nw', padx=20, pady=10)

stereometryFrame = Frame(root, borderwidth=3, relief=SOLID)
stereometryLabel = Label(stereometryFrame, text='Стереометрия', font=('Arial', '14', 'bold'), width=50, height=15, anchor='nw', padx=20, pady=10)

# UI pack
helloLabel.pack()

planemetryFrame.pack(anchor='w', pady=20, padx=20)
planemetryLabel.pack()

stereometryFrame.pack(anchor='w', pady=20, padx=20)
stereometryLabel.pack()

#buttons creating + packing

i = 0
for r in range(3):
    for c in range(3):
        button = Button(planemetryFrame, text=categoryName[i], width=12)
        button.pack()
        i+=1



# open the window
root.mainloop()