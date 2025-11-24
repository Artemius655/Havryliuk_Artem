from tkinter import *

def on_key_press(event):
    label.pack(pady=50)

labuba = Tk()
labuba.title("Вікно №2")  # <-- Виправлено
labuba.geometry("500x500")

label = Label(labuba,text="Функція виконана",font=("Calibri", 14),fg="white",bg="green"
)

labuba.bind("<KeyPress>", on_key_press)
labuba.mainloop()