import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class demo:
    def search(self):
        self.t1.delete((*self.t1.get_children()))

        conn = sqlite3.connect("mydata.sqlite3")
        s = "select * from programs"
        cr = conn.cursor()
        cr.execute(s)

        ans = cr.fetchall()

        i=0
        for r in ans:
            if self.txt1.get() in r[0]:
                self.t1.insert("",index=i,values=r)
    def __init__(self):
        self.root=Tk()

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)

        self.t1=Treeview(self.p1,columns=("degree","description"))
        self.t1.heading("degree",text="DEGREE NAME")
        self.t1.heading("description",text="PROGRAM DESCRIPTION")

        self.t1["show"]="headings"

        conn=sqlite3.connect("mydata.sqlite3")
        s="select * from programs"
        cr=conn.cursor()
        cr.execute(s)

        ans=cr.fetchall()

        i=0
        for r in ans:
            self.t1.insert("",index=i,values=r)
        self.t1.pack()

        self.lb1=Label(self.p2,text="Enter Search")
        self.txt1=Entry(self.p2)

        self.bt1=Button(self.p2,text="Search",command=self.search)

        self.lb1.grid(row=0,column=0)
        self.txt1.grid(row=0,column=1)
        self.bt1.grid(row=0,column=2)

        self.p1.pack()
        self.p2.pack()

        self.root.mainloop()
#------------------------------------------------
