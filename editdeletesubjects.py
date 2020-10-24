import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo

from tkinter.ttk import *

class demo:

    def remove(self):
        s="delete from subjects where subjectcode ='"+self.cb1.get()+"'"
        self.cr.execute(s)
        self.conn.commit()
        showinfo("Time Table Management","Remove Successfully")


    def save(self):

        k = "update subjects set subjectname=' "+self.txt.get()+ " ' where subjectcode='"+self.cb1.get()+"'"
        self.cr.execute(k)
        self.conn.commit()
        showinfo("TIMETABLE MANAGEMENT","SAVED SUCCESSFULLY")




    def __init__(self):

        self.root=Tk()
        self.root.geometry("600x400")

        p=["Select Subject"]
        self.conn=sqlite3.connect("mydata.sqlite3")
        s="select * from subjects"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        result=self.cr.fetchall()

        for r in result:
            p.append(r[0])


        self.lb1=Label(self.root,text="Subjectcode")
        self.cb1=Combobox(self.root,values=p,state="readonly",text="Select Subjectcode")

        self.lb2=Label(self.root,text="Semester")
        self.cb2=Combobox(self.root,values=(1,2,3,4,5,6,7,8,9,10,11),state="readonly")

        self.cb1.current(0)
        self.bt1=Button(self.root,text="Search",command=self.save)

       # self.lb2=Label(self.root,text="subjectcode")
        self.lb3=Label(self.root,text="subjectname")
        #self.cb3=Combobox(self.root,text="Select subjectcode")
        #self.cb4=Combobox(self.root,text="Select subjectname")

        self.txt=Entry(self.root)

        self.bt2=Button(self.root,text="Delete",command=self.remove)
        self.bt3=Button(self.root,text="save",command=self.save)






        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)

        self.lb2.grid(row=1, column=0)
        self.cb2.grid(row=1,column=1)

        #self.cb3.grid(row=1, column=0)
        #self.cb4.grid(row=2, column=0)

        self.lb3.grid(row=2,column=0)
        self.txt.grid(row=2,column=1)

        self.bt2.grid(row=3,column=1)
        self.bt3.grid(row=3,column=2)



        self.root.mainloop()
#-------------------------------------


