from tkinter import *

window=Tk()
window.wm_title("IQC Check")
l1=Label(window, text="Name")
l1.grid(row=0, column=0)

l2=Label(window, text="User")
l2.grid(row=0, column=1)

l3=Label(window, text="Date")
l3.grid(row=0, column=2)

l4=Label(window, text="PG ID")
l4.grid(row=0, column=3)

l5=Label(window, text="Feature ID")
l5.grid(row=0, column=4)

l6=Label(window, text="JIRA ID")
l6.grid(row=0, column=5)

l7=Label(window, text="Rating")
l7.grid(row=0, column=6)

l8=Label(window, text="PG Update")
l8.grid(row=0, column=7)

l9=Label(window, text="Manager")
l9.grid(row=0, column=8)

e1_name=StringVar()
e1=Entry(window, textvariable="e1_name")
e1.grid(row=1, column=0)

e2_user=StringVar()
e2=Entry(window, textvariable="e2_user")
e2.grid(row=1, column=1)

e3_date=StringVar()
e3=Entry(window, textvariable="e3_date")
e3.grid(row=1, column=2)

e4_pgid=StringVar()
e4=Entry(window, textvariable="e4_pgid")
e4.grid(row=1, column=3)

e5_featureid=StringVar()
e5=Entry(window, textvariable="e5_featureid")
e5.grid(row=1, column=4)

e6_jiraid=StringVar()
e6=Entry(window, textvariable="e6_jiraid")
e6.grid(row=1, column=5)

e7_rating=StringVar()
e7=Entry(window, textvariable="e7_rating")
e7.grid(row=1, column=6)

e8_pgupdate=StringVar()
e8=Entry(window, textvariable="e8_pgupdate")
e8.grid(row=1, column=7)

e9_manager=StringVar()
e9=Entry(window, textvariable="e9_manager")
e9.grid(row=1, column=8)

b1=Button(window, text="View ALL", width=15)
b1.grid(row=2, column=9)

b2=Button(window, text="Search", width=15)
b2.grid(row=3, column=9)

b3=Button(window, text="Add", width=15)
b3.grid(row=4, column=9)

b4=Button(window, text="Update", width=15)
b4.grid(row=5, column=9)

b5=Button(window, text="Delete", width=15)
b5.grid(row=6, column=9)

b6=Button(window, text="Close", width=15)
b6.grid(row=7, column=9)

list1=Listbox(window, height=12, width=190)
list1.grid(row=2, column=0, columnspan=8, rowspan=8)

sb1=Scrollbar(window)
sb1.grid(row=2, column=8, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()