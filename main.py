#On this page I'm creating main structur and logic for Delta
from tkinter import *
import getpass
from menuCommands import *
from pagesArray import pagesArray

name = getpass.getuser()
categoryName = ['Основы', 'Квадрат', 'Прямоугольник', 'Треугольник', 'Пр. треугольник', 'Окружность', 'Параллелограмм',
                'Ромб', 'Трапеция', 'Основы', 'Куб', 'Параллелепипед', 'Призмы', 'Цилиндр', 'Пирамиды', 'Конусы', 'Шар', 'Тетраэдр']


# window settings
root = Tk()
root.title('𝕯𝖊𝖑𝖙𝖆')

createMenu(root)
# window settings


# UI creating
helloLabel = Label(root, text=f'Привет, {name}. Это Delta.',
                   font=('Times New Roman', '20', 'bold'), fg='slate gray')
helloLabelText = Label(root, text='Система-помощник для изучения геометрии',
                       font=('Times New Roman', '13'), fg='light slate gray')

planemetryFrame = Frame(root, bg='light slate gray', padx=30, pady=30)
planemetryFrame.pack_propagate(False)
planemetryLabel = Label(root, text='Планиметрия',
                        font=('Arial', '13', 'normal'), fg='slate gray')


stereometryFrame = Frame(root, bg='light slate gray', padx=30, pady=30)
stereometryFrame.pack_propagate(False)
stereometryLabel = Label(root, text='Стереометрия',
                         font=('Arial', '13', 'normal'), fg='slate gray')
# UI creating




# UI pack
helloLabel.pack(pady=(24, 0))
helloLabelText.pack()

planemetryLabel.pack(anchor='nw', padx=22, pady=(20, 0))
planemetryFrame.pack(anchor='w', pady=(4, 20), padx=20)

stereometryLabel.pack(anchor='nw', padx=22)
stereometryFrame.pack(anchor='w', pady=(4, 20), padx=20)
# UI pack


# buttons creating + packing
i = 0
for r in range(3):
    for c in range(3):
        button = Button(planemetryFrame,
                        text=categoryName[i], width=16, padx=4, pady=4, borderwidth=0, command=pagesArray[i].createPage)
        button.grid(row=r, column=c, padx=3, pady=3)
        i += 1

for r in range(3):
    for c in range(3):
        button = Button(stereometryFrame,
                        text=categoryName[i], width=16, padx=4, pady=4, borderwidth=0, command=pagesArray[i].createPage)
        button.grid(row=r, column=c, padx=3, pady=3)
        i += 1
# buttons creating + packing


# open the window
root.mainloop()
