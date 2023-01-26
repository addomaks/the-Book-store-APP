from tkinter import *

window=Tk()
def converter():
   gram=float(e1_value.get())*1000
   pound=float(e1_value.get())*2.20
   ounce=float(e1_value.get())*35.27
   t1.delete("1.0", END)
   t1.insert(END, gram)
   t2.delete("1.0", END)
   t2.insert(END, pound)
   t3.delete("1.0", END)
   t3.insert(END, ounce)


e1_value=StringVar()
e1=Entry(window, textvariable=(e1_value))
e1.grid(row=0, column=2)

b1=Button(window, text="convert",command=converter)
b1.grid(row=0,column=3)

p1=Label(text="KiloGram(KG)")
p1.grid(row=0, column=1)

p2=Label(window, text="Grams")
p2.grid(row=1, column=1)

p3=Label(window, text="Pounds")
p3.grid(row=1, column=2)

p4=Label(window, text="Ounces")
p4.grid(row=1, column=3)

t1=Text(window, height=1,width=20)
t1.grid(row=2, column=1)

t2=Text(window, height=1,width=20)
t2.grid(row=2, column=2)

t3=Text(window, height=1,width=20)
t3.grid(row=2, column=3)

window.mainloop()

