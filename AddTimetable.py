import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo

from tkinter.ttk import *

class addtimetabele:
    def addrow(self):
        p = "insert into timetable values(NULL,'" + self.cb3.get() + "','" + self.cb4.get() + "','" + self.cb5.get() + "','" + self.txt.get() + "')"
        self.cr.execute(p)
        self.conn.commit()
        showinfo("", "Time Table Added Successfully")
    def getdata(self,d):
        s="select subjectcode from subjects"
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]

        for r in ans:
            x.append(r[0])
        self.cb3.config(values=x)


    def __init__(self):

        self.root=Tk()

        self.lb1=Label(self.root,text="Select Program")
        self.lb2=Label(self.root,text="Select Semester")
        self.lb3=Label(self.root,text="Select Subject Code")
        self.lb4=Label(self.root,text="Select Day of Week")
        self.lb5=Label(self.root,text="Select Slot")
        self.lb6=Label(self.root,text="Enter Teacher Name")

        self.conn=sqlite3.connect("mydata.sqlite3")
        self.cr=self.conn.cursor()
        s="select degreename from programs"
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]
        for r in ans:
            x.append(r[0])

        self.cb1=Combobox(self.root,values=x,state="readonly")
        self.cb2=Combobox(self.root,values=(1,2,3,4,5,6,7,8,9,10,11),state="readonly")
        self.cb2.bind("<<ComboboxSelected>>",self.getdata)
        self.cb3=Combobox(self.root,state="readonly")
        self.cb4=Combobox(self.root,state="readonly",values=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"))
        self.cb5=Combobox(self.root,state="readonly",values=("10Am-11Am","11Am-12Noon","12Noon-1Pm","2Pm-3Pm","3Pm-4Pm"))
        self.txt=Entry(self.root)
        self.txt2=Entry(self.root)

        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)

        self.lb2.grid(row=1,column=0)
        self.cb2.grid(row=1,column=1)

        self.lb3.grid(row=2,column=0)
        self.cb3.grid(row=2,column=1)

        self.lb4.grid(row=3,column=0)
        self.cb4.grid(row=3,column=1)

        self.lb5.grid(row=4,column=0)
        self.cb5.grid(row=4,column=1)

        self.lb6.grid(row=5,column=0)
        self.txt.grid(row=5,column=1)

        self.bt1=Button(self.root,text="Add New Data",command=self.addrow)

        self.bt1.grid(row=6,column=1)

        self.root.mainloop()
#-------------------------------------
