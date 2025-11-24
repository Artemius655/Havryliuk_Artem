from tkinter import*
from tkinter import messagebox
def change ( event ):
    s=int(entry.get())
    r=s*s
    messagebox.showinfo("добуток", f"Добуток числа на нього самого: {r}")
    
labuba=Tk()
labuba.title("Це є вікно :)")
labuba.geometry("875x578")
labuba["bg"]="#6075EB"
labuba.resizable(0,0)

entry=Entry(labuba, bg="white", width="35", font="Calibri 13") 
entry.place(x=100,y=100)

but=Button(labuba, bg="white", text="Ок", fg="black", font="Calibri 13")
but.place(x=100, y=140)

label=Label(labuba, text="Введіть ціле число", bg="white", fg="black", font="Calibri 13")
label.place(x=100,y=50)

but.bind("<Button-3>",change)
labuba.mainloop()