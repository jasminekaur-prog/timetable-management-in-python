from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo
from tkinter.ttk import *

class demo:
    def showdata(self):
        self.t1.delete(*self.t1.get_children())

        s="select * from subjects where degreename='"+self.cb1.get()+"' and  semester="+self.cb2.get()

        self.cr.execute(s)
        ans=self.cr.fetchall()

        i=0
        for  r in ans:
           self.t1.insert("",index=i,values=r)



    def __init__(self):
        self.root=Tk()
        self.conn = sqlite3.connect("mydata.sqlite3")

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)

        self.lb1=Label(self.p1,text="Select Degree Code")

        s="select degreename from programs"
        self.cr=self.conn.cursor()
        self.cr.execute(s)

        ans=self.cr.fetchall()

        x=[]

        for r in ans:
            x.append(r[0])


        self.cb1=Combobox(self.p1,values=x,state="readonly")
        self.cb2=Combobox(self.p1,values=(1,2,3,4,5,6,7,8,9,10,11),state="readonly")

        self.bt1=Button(self.p1,text="Submit",command=self.showdata)

        self.t1=Treeview(self.p2,columns=("subjectcode","subjectname","semester","degree"))

        self.t1.heading("subjectcode",text="Subject Code")
        self.t1.heading("subjectname",text="Subject Name")
        self.t1.heading("semester",text="Semester")
        self.t1.heading("degree",text="Degree Name")
        self.t1["show"]="headings"

        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)
        self.cb2.grid(row=0,column=2)
        self.bt1.grid(row=0,column=3)
        self.t1.pack()


        self.p1.pack()
        self.p2.pack()




        self.root.mainloop()
#-----------------------------------------
