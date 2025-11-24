from tkinter import *
def change(event):
    labuba.geometry("300x200")
    labuba["bg"] = "yellow"
    labuba.title("Artem Havryliuk")
    labuba.minsize("200x100")
    labuba.maxsize("1000x900")
    
labuba = Tk()
labuba.bind("<KeyPress>",change)
labuba.mainloop()