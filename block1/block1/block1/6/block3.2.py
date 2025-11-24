from tkinter import *
from tkinter import messagebox
def change(event):
    
    labuba["bg"] = "purple"
    labuba.geometry("650x560")
    but.config(bg="yellow")
    messagebox.showinfo("Повідомлення","Завдання виконано!")
labuba = Tk()
labuba.geometry("500x800")
labuba.title("Вікно №2")
but = Button(labuba, width=4,height=2,bg="green",text = "Ок", fg="black",font="Times 12")
but.place (x=200,y=390)
but.bind("<Button-1>",change)
labuba.mainloop()