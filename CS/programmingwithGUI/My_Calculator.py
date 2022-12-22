from tkinter import *
from math import *


def setClear() -> None:
    """

    :rtype: None
    """
    display.delete(0, 'end')

class Calculator:
    def __init__(self, string: str):
        self.string = string
        
    def sin(self, string):
        setClear()
        return sin(radians(int(string)))
    
    def cos(self, string):
        setClear()
        return cos(radians(int(string)))
    
    def sqrt(self, string):
        setClear()
        return ceil(sqrt((float(string))))
    
    def log(self, string):
        setClear()
        return ceil(log(float(string)))
    
    def result(self, string):
        setClear()
        return eval(string)
        
calculator = Calculator("Initializing")


def push(key):
    display.insert('end', key)
window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)
button_list = ['7', '8', '9', '/', 'C', 'sin',
               '4', '5', '6', '*', 'del', 'cos',
               '1', '2', '3', '-', '🥧', 'sqrt',
               '0', '.', '=', '+', 'e', 'log'
               ]
row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        print(f"[정보] input = {t}")
        if t == "C":
            setClear()
        elif t == "del":
            display.delete(len(display.get())-1, 'end')
        elif t == "🥧":
            display.insert('end', "3.14")
        elif t == "e":
            display.insert('end', "2.71")
        elif t == "=":
            display.insert('end', calculator.result(display.get()))
        elif t == "sin":
            display.insert(0, calculator.sin(display.get()))
        elif t == "cos":
            display.insert(0, calculator.cos(display.get()))
        elif t == "sqrt":
            display.insert(0, calculator.sqrt(display.get()))
        elif t == "log":
            display.insert(0, calculator.log(display.get()))
        else:
            push(t)
    Button(window, text=button_text, width=5, command=process).grid(
        row=row_index, column=col_index)
    col_index += 1
    if col_index > 5:
        row_index += 1
        col_index = 0
window.mainloop()
