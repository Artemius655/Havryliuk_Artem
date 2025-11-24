from tkinter import *
from tkinter import messagebox

def change(event):
    labuba.geometry("560x435")
    labuba.config(bg="blue")
    label1 = Label(labuba, text = "Це вікно було створено в середовищі IDLE", font = "Arial 14", fg = "white", bg = "blue")
    label1.place(x = 200, y = 250)
labuba = Tk()

labuba.title("Вікно №3")
labuba.geometry("500x500") 
but = Button(labuba,text="Розфарбуй",bg="pink",fg="blue")
but.bind("<Button-3>", change)
but.place (x=200,y=200)

labuba.mainloop()