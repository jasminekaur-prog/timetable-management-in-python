from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo
from tkinter.ttk import *

class demo:
    def insert(self):
        s="insert into subjects values("+self.txt1.get()+",'"+self.txt2.get()+"',"+self.txt3.get()+",'"+self.txt4.get()+"')"

        self.cr.execute(s)
        self.conn.commit()
        self.conn.close()
        showinfo("","Subject Added Successfully")


    def __init__(self):
        self.root=Tk()
        self.conn = sqlite3.connect("mydata.sqlite3")

        self.lb1=Label(self.root,text="Enter Subject Code")
        self.lb2=Label(self.root,text="Enter Subject Name")
        self.lb3 = Label(self.root, text="Enter Semester")
        self.lb4 = Label(self.root, text="Enter Degree Name")

        self.txt1=Entry(self.root)
        self.txt2=Entry(self.root)
        self.txt3=Entry(self.root)

        s="select degreename from programs"
        self.cr=self.conn.cursor()
        self.cr.execute(s)

        ans=self.cr.fetchall()

        x=[]

        for r in ans:
            x.append(r[0])


        self.txt4=Combobox(self.root,values=x,state="readonly")

        self.bt1=Button(self.root,text="Submit",command=self.insert)

        self.lb1.grid(row=0,column=0)
        self.txt1.grid(row=0,column=1)

        self.lb2.grid(row=1,column=0)
        self.txt2.grid(row=1,column=1)

        self.lb3.grid(row=2,column=0)
        self.txt3.grid(row=2,column=1)

        self.lb4.grid(row=3,column=0)
        self.txt4.grid(row=3,column=1)

        self.bt1.grid(row=4,column=1)


        self.root.mainloop()
#-----------------------------------------
