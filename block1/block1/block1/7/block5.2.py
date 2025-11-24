from tkinter import*
from tkinter import messagebox
def change ( event ):
    label["text"]=entry.get()
    messagebox.showinfo("Підтвердження події","Дія виконана!")
labuba=Tk()
labuba.title("Перше вікно")
labuba.geometry("600x600")
labuba["bg"]="#94960C"
labuba.resizable(0,0)
entry=Entry(labuba, bg="white", width="30", font="Calibri 12") 
entry.place(x=180,y=350)
label=Label(labuba, text="Ви нічого не ввели", bg="#C19494", fg="#150A76", font="Calibri 12")
label.place(x=250,y=300)
labuba.bind("<Button-3>",change)
labuba.mainloop()