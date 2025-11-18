from tkinter import *
from tkinter import messagebox
def change(event):
    labuba.geometry("500x600")
    labuba["bg"] = "grey"
    labuba.title("ІПЗ - 2/2")
    labuba.minsize("400x500")
    labuba.maxsize("900x1000")

def change1(event):
    messagebox.showinfo("Повідомлення","Я навчаюся у 8 класі!")
labuba = Tk()
labuba.bind("<KeyPress>",change)
labuba.bind("<Button-1>",change1)
labuba.mainloop()