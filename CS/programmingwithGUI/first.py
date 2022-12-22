from tkinter import *

txt = "학과:  이름: "


if __name__ == '__main__':
    window = Tk()
    window.title("경상국립대학교")
    l1 = Label(window, text="학과")
    e1 = Entry(window)
    l2 = Label(window, text="이름")
    e2 = Entry(window)
    l3 = Label(window, text="학과:  이름: ")

    def process():
        global txt
        l3.config(text = f"학과: {e1.get()} 이름: {e2.get()} ")
    b1 = Button(window, text="확인", command=process)
    
    l1.pack(); e1.pack(); l2.pack(); e2.pack(); l3.pack(); b1.pack()
    
    window.mainloop()
