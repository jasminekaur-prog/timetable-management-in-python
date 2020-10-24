import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo

from tkinter.ttk import *

class demo:

    def remove(self):
        s="delete from timetable where subjectcode ='"+self.cb1.get()+"'"
        self.cr.execute(s)
        showinfo("Time Table Management","Remove Successfully")

    def save(self):

        k = "update timetable set teachername=' "+self.txt.get()+ " ' where subjectcode='"+self.cb1.get()+"'"
        self.cr.execute(k)
        self.conn.commit()
        showinfo("TIMETABLE MANAGEMENT","SAVED SUCCESSFULLY")

    def __init__(self):
            self.root = Tk()
            self.root.geometry("600x400")

            p = ["Select Subject"]
            q =["Select Teacher's Name"]
            self.conn = sqlite3.connect("mydata.sqlite3")
            s = "select * from timetable"
            self.cr = self.conn.cursor()
            self.cr.execute(s)
            result = self.cr.fetchall()

            for r in result:
                p.append(r[0])


            self.lb1 = Label(self.root, text="Subjectcode")
            self.cb1 = Combobox(self.root, values=p, state="readonly", text="Select Subjectcode")

            self.lb2=Label(self.root,text="Semester")
            self.cb2=Combobox(self.root,values=(1,2,3,4,5,6,7,8,9,10,11),state="readonly")

            self.lb3=Label(self.root,text="Day of Week")
            self.cb3 = Combobox(self.root, values=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"), state="readonly")

            self.lb4=Label(self.root,text="Slot")
            self.cb4 = Combobox(self.root, values=("10Am-11Am","11Am-12Noon","12Noon-1Pm","2Pm-3Pm","3Pm-4Pm"), state="readonly")

            self.lb5=Label(self.root,text="Teacher's Name")
            self.txt=Entry(self.root)

            self.cb1.current(0)



            self.bt2 = Button(self.root, text="Delete", command=self.remove)
            self.bt3= Button(self.root, text="Save", command=self.save)


            self.lb1.grid(row=0, column=0)
            self.cb1.grid(row=0, column=1)

            self.lb2.grid(row=1, column=0)
            self.cb2.grid(row=1, column=1)

            self.lb3.grid(row=2, column=0)
            self.cb3.grid(row=2, column=1)

            self.lb4.grid(row=3, column=0)
            self.cb4.grid(row=3, column=1)

            self.lb5.grid(row=4, column=0)
            self.txt.grid(row=4, column=1)

            self.bt2.grid(row=5, column=1)
            self.bt3.grid(row=5,column=2)


            self.root.mainloop()
    # -------------------------------------


