import sqlite3
from tkinter import *
from tkinter.ttk import*
from tkinter.messagebox import *

class demo:
    def test(self):
        conn = sqlite3.connect("mydata.sqlite3")

        ps = "select * from programs"
        cr = conn.cursor()
        cr.execute(ps)
        ans = cr.fetchall()

        flag=False

        for r in ans:
            if str(r[0]).upper==self.txt1.get().upper():
                flag=True
                break

        if flag==True:
            showinfo(""," DUPLICATE COURSE NAME")

        elif self.txt1.get()=="" or self.txt2.get()=="":
            showinfo("","cannot leave any field blank")

        else:
            s="insert into programs values(' "+self.txt1.get()+"','"+self.txt2.get()+" ' )"

            cr.execute(s)
            conn.commit()
            showinfo("","PROGRAM ADDED SUCCESSFULLY")
    def __init__(self):
        self.root=Tk()

        self.lb1=Label(self.root,text="Degree")
        self.txt1=Entry(self.root)

        self.lb2=Label(self.root,text="Description")
        self.txt2=Entry(self.root)

        self.bt1=Button(self.root,text="Submit",command=self.test)


        self.lb1.grid(row=0,column=0)
        self.txt1.grid(row=0,column=1)
        self.lb2.grid(row=1,column=0)
        self.txt2.grid(row=1,column=1)

        self.bt1.grid(row=2,column=2)

        self.root.mainloop()