#About Delta page
from tkinter import *



def createAboutProjectPage():
    aboutWindow = Tk()
    aboutWindow.title('О Проекте')
    aboutWindow.geometry('400x600')
    aboutWindow.mainloop()
    
    aboutLabel = Label(aboutWindow, text='Delta - это:', font=('Times New Roman', '20', 'bold'), fg='slate gray')
    
    
    aboutLabel.pack()