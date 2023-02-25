# About Delta page
from tkinter import *


def createAboutProjectPage():
    aboutWindow = Tk()
    aboutWindow.title('О Проекте')
    aboutWindow.geometry('400x470')

    aboutLabel = Label(aboutWindow, text='Delta - это:',
                       font=('Times New Roman', '20', 'bold'), fg='slate gray')
    mainTextEng = Text(aboutWindow, font=('Arial', '12'),
                    width=46, height=7, wrap=WORD)
    mainTextEng.insert(INSERT, "Delta is an assistant system that will help you optimize your knowledge of geometry and fill in gaps in specific topics. Delta presents the main and most important knowledge, terms, theorems and axioms of the two main sections of geometry, useful calculators, and much more. All of this is Delta.")
    mainTextEng.configure(state='disabled')
    mainTextRu = Text(aboutWindow, font=('Arial', '12'),
                    width=46, height=7, wrap=WORD)
    mainTextRu.insert(INSERT, "Дельта - система помощник, которая поможет оптимизировать Ваши знания в геометрии и восполнить пробелы в конкретных темах. В Delt'е представлены главные и самые важные знания, термины, теоремы и аксиомы двух главных разделов геометрии, полезные калькуляторы и многое другое. Все это - Delta.")
    mainTextRu.configure(state='disabled')
    
    GitHubLabel = Label(aboutWindow, text='Ссылка на GitHub проекта:', font=('Times New Roman', '14'), fg='gray')
    GitHubUrl = Label(aboutWindow, text='https://github.com/mikaeloganesian/Delta', font=(
            'Times New Roman', '14', 'bold'), fg='blue')

    aboutLabel.pack(pady=(10, 0))
    mainTextRu.pack(padx=20, pady=15)
    mainTextEng.pack(padx=20, pady=15)
    GitHubLabel.pack(pady=(10, 0))
    GitHubUrl.pack()

    aboutWindow.mainloop()
