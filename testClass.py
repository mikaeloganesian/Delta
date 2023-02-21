from tkinter import *
from PIL import Image, ImageTk

class page():
    def __init__(self, title, pageTitle, mainText, imageURL): 
        self.title = title
        self.pageTitle = pageTitle
        self.mainText = mainText
        self.imageURL = imageURL
    
    def createPage(self):
            window = Tk()                   #window creating
            window.title(self.title)
            window.geometry('400x400')
            
            title = Label(window, text=self.pageTitle, font=('Times New Roman', '20'), fg='slate gray', pady=6)      #title creating
            title.pack()

            mainText = Text(window, font=('Arial', '14'), width=46, wrap=WORD, fg='slate gray')
            mainText.insert(INSERT, self.mainText)
            mainText.configure(state='disabled')
            mainText.pack()                 #main text creating

