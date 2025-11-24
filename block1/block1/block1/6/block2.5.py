from tkinter import *
def change(event):
    labuba.geometry("400x300")
    labuba["bg"] = "green"
    labuba.title("Вікно №2")
    

labuba = Tk()
labuba.bind("<Button-1>",change)

labuba.geometry("700x400")
labuba["bg"] = "red"
labuba.title("Вікно №1")
labuba.mainloop()