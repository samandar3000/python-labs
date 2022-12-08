
from tkinter import *

root = Tk()

A = True; B = False

def analyse(exp):
    test = str(exp)
    Label(root, text = test, fg = "red").pack()
    
def evaluate(evl):
    a = str(evl)
    a = eval(a)
    Label(root, text = a).pack()

myLabel = Label(root, text ="ЛОГИЧЕСКИЕ ОПАРАТОРЫ", width = 200, height = 3, fg = "blue")

myLabel.pack()


button1 = Button(root, text ="A and B", command=lambda:analyse(A and B)).pack()

button2 = Button(root, text ="(A and B) or B)", command=lambda:analyse((A and B) or B)).pack()

button3 = Button(root, text ="(A and B) or not (A and B)", command=lambda:analyse((A and B) or not (A and B))).pack()

button4 = Button(root, text = "A and B or not (A or B) or B", command=lambda:analyse(A and B or not (A or B) or B)).pack()

button5 = Button(root, text="B and B or not A and (A or B or A) or not (A or B)", command =lambda:analyse(B and B or not A and (A or B or A) or not (A or B))).pack()


button7 = Button(root, text ="1 << 2", command=lambda:evaluate(1 << 2)).pack()

button8 = Button(root, text = "1 & 0 | 1 >> 1", command=lambda:evaluate(1 & 0 | 1 >> 1)).pack()

button9 = Button(root, text = "1 & 0 | 1 >> 0", command=lambda:evaluate(1 & 0 | 1 >> 0)).pack()

button10 = Button(root, text = "0b101 & 0b111 ^ 0b111 | 0b010)", command=lambda:evaluate(0b101 & 0b111 ^ 0b111 | 0b010)).pack()


root.mainloop()
