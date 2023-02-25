from tkinter import *

class stereometryCalc():
    def __init__(self, dataA, dataB):
        self.dataA = dataA
        self.dataB = dataB
        self.S = self.dataA*self.dataB
        self.P = (self.dataA + self.dataB)*2


testWindow = Tk()
testWindow.title('Stereometry Calculator')
testWindow.geometry('500x500')

label = Label(testWindow, text='Введите данные и выберите функцию:', font=('Times New Roman', '20'))
label.pack()

result = Label(testWindow, text= "Площадь вашего квадрата = " + str(stereometryCalc(10, 15).S))
result.pack()

testWindow.mainloop()