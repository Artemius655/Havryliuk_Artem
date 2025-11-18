from tkinter import*
def change ( event ):
    label["text"]=entry.get()

labuba=Tk()
labuba.title("Вікно №3")
labuba.geometry("600x700")
labuba["bg"]="#BD5252"
labuba.resizable(0,0)

entry=Entry(labuba, bg="white", width="30", font="Calibri 13") 
entry.place(x=180,y=350)
but=Button(labuba, bg="white", text="Ок", fg="black", font="Calibri 13")
but.place(x=300, y=400)
label=Label(labuba, text="Ви нічого не ввели", bg="white", fg="black", font="Calibri 13")
label.place(x=250,y=300)

but.bind("<Button-3>",change)
labuba.mainloop()