from tkinter import *
labuba = Tk()
labuba.geometry("500x500")
labuba.title("Вікно №1")
label1 = Label(labuba, text = "Це вікно було створено в середовищі IDLE", font = "Arial 14", fg = "blue")
label1.place(x = 60, y = 40)
labuba.mainloop()