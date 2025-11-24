from tkinter import *
from tkinter import messagebox

def change(event):
    labuba.geometry("560x435")
    labuba.config(bg="yellow")
    messagebox.showinfo("Виконано", "Зміни застосовані!")

labuba = Tk()

labuba.title("Це вікно Python")
labuba.geometry("300x200") 
but = Button(labuba,text="Змінити",bg="pink",fg="blue")
but.bind("<Button-3>", change)
but.place (x=125,y=100)

labuba.mainloop()