from tkinter import *
from tkinter import messagebox
def newtext (event):
    if prap1.get()==1 and prap3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво у маленькому ріжку")
    elif prap1.get()==1 and prap4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво у середньому ріжку")
    elif prap1.get()==1 and prap6.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво у великокому ріжку")
    elif prap2.get()==1 and prap3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво у маленькому ріжку")
    elif prap2.get()==1 and prap4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво у середньому ріжку")
    elif prap2.get()==1 and prap6.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво у великокому ріжку")
    elif prap5.get()==1 and prap3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво у маленькому ріжку")
    elif prap5.get()==1 and prap4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво у середньому ріжку")
    elif prap5.get()==1 and prap6.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво у великокому ріжку")

labuba=Tk()
labuba.geometry("400x400")
labuba.title("Магазин морозива")
label=Label (labuba, text="Оберіть тип морозива")
label.place ( x = 100 , y = 80 )
label1=Label (labuba, text="Оберіть розмір ріжку")
label1.place ( x = 100 , y = 180 )
prap1=IntVar()
prap2=IntVar()
prap3=IntVar()
prap4=IntVar()
prap5=IntVar()
prap6=IntVar()


pr1=Radiobutton (labuba, text="Ванільне", variable=prap1, onvalue=1, offvalue=0)
pr1.place ( x = 100 , y = 100 )

pr2=Radiobutton (labuba, onvalue=1, offvalue=0, text="Шоколадне", variable=prap2,)
pr2.place ( x = 100 , y = 120 )
pr5=Radiobutton (labuba, onvalue=1, offvalue=0, text="Фруктове", variable=prap5,)
pr5.place ( x = 100 , y = 140 )

pr3=Radiobutton (labuba, text="Маленький", variable=prap3, onvalue=1, offvalue=0)
pr3.place (x=100, y=200)

pr4=Radiobutton (labuba, onvalue=1, offvalue=0, text="Середній", variable=prap4,)
pr4.place (x=100, y=220)

pr6=Radiobutton (labuba, onvalue=1, offvalue=0, text="Великий", variable=prap6,)
pr6.place (x=100, y=240)

but=Button(labuba, bg="white", text="Ок", fg="black", font="Calibri 13",)
but.place(x=100, y=260)

but.bind("<Button-1>", newtext)
labuba.mainloop()