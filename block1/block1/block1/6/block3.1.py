from tkinter import *
def change(event):
    
    labuba["bg"] = "green"
    labuba.geometry("650x560")
    but.config(bg="blue")

labuba = Tk()
labuba.geometry("400x300")
but = Button(labuba, width=8,height=2,bg="green",text = "Розфарбуй", fg="red",font="Times 12")
but.place (x=100,y=90)
but.bind("<Button-1>",change)
labuba.mainloop()