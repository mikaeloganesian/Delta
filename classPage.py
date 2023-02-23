from tkinter import *


class page():
    def __init__(self, title, pageTitle, mainText, imageURL, seeMoreUrl):
        self.title = title
        self.pageTitle = pageTitle
        self.mainText = mainText
        self.imageURL = imageURL
        self.seeMoreUrl = seeMoreUrl

    def createPage(self):
            window = Tk()                   #window creating
            window.title(self.title)
            window.geometry('400x400')

            title = Label(window, text=self.pageTitle, font=('Times New Roman', '20'), fg='slate gray', pady=6)      #title creating
            title.pack()

            mainText = Text(window, font=('Arial', '14'), width=46, height=16, wrap=WORD)
            mainText.insert(INSERT, self.mainText)
            mainText.configure(state='disabled')
            mainText.pack(padx=20)                 #main text creating

            mainTextScrollBar = Scrollbar(orient='vertical', command=mainText.yview)
            mainTextScrollBar.pack(side=RIGHT, fill=Y)
            mainText["yscrollcommand"]=mainTextScrollBar.set

            seeMore = Label(window, text='Смотреть подробнее:', font=('Times New Roman', '14'), fg='gray')
            seeMoreUrl = Label(window, text=self.seeMoreUrl, font=('Times New Roman', '14', 'bold'), fg='blue')
            seeMore.pack(pady=(10, 0))
            seeMoreUrl.pack()
