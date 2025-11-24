from tkinter import *
def change(event):
    labuba.geometry("700x600")
    labuba["bg"] = "thistle"
    labuba.resizable(0,0)
    labuba.title("RFCIT")
    
labuba = Tk()
labuba.bind("<Button-3>",change)
labuba.mainloop()