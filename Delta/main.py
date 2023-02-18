from tkinter import *


def finish():
    root.destroy()
    print('Закрытие приложения')

# window settings
root = Tk()
root.title('Delta - шпаргалка по геометрии')
root.geometry('500x500')
root.maxsize(750, 750)
root.protocol('WM_DELETE_WINDOW', finish)
root.attributes('-alpha', 0.5)

# UI inicializating
label = Label(text='Hello, this is Delta')
label.pack()


# open the window
root.mainloop()