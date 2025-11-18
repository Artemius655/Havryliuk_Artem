from tkinter import *
def change(event):
    labuba.geometry("400x300")
    labuba["bg"] = "green"
    labuba.title("Rivne")
    
labuba = Tk()
labuba.bind("<Button-1>",change)
labuba.mainloop()