from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo
from tkinter.ttk import *

class demo:
    def showdata(self):
        self.t1.delete(*self.t1.get_children())
        days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        slot1=["10Am-11Am"]

        for day in days:
            s="select timetable.teachername,timetable.subjectcode,subjects.subjectname,timetable.dayofweek from timetable,subjects where subjects.subjectcode=timetable.subjectcode and timetable.slot='10Am-11Am' and subjects.degreename='"+self.cb1.get()+"' and subjects.semester="+self.cb2.get()+" and dayofweek='"+day+"'"

            self.cr.execute(s)

            ans=self.cr.fetchone()
            if ans!=None:
               slot1.append(str(ans[0])+","+str(ans[1])+","+str(ans[2]))
            else:
               slot1.append("Free Lecture")

            print(slot1)

        self.t1.insert("",index=0,values=slot1)


        slot2=["11Am-12Noon"]

        for day in days:
            s="select timetable.teachername,timetable.subjectcode,subjects.subjectname,timetable.dayofweek from timetable,subjects where subjects.subjectcode=timetable.subjectcode and timetable.slot='11Am-12Noon' and subjects.degreename='"+self.cb1.get()+"' and subjects.semester="+self.cb2.get()+" and dayofweek='"+day+"'"

            self.cr.execute(s)

            ans=self.cr.fetchone()
            if ans!=None:
               slot2.append(str(ans[0])+","+str(ans[1])+","+str(ans[2]))
            else:
                slot2.append("Free Lecture")

            print(slot2)

        self.t1.insert("",index=1,values=slot2)
        slot3 = ["12Noon-1Pm"]

        for day in days:
            s = "select timetable.teachername,timetable.subjectcode,subjects.subjectname,timetable.dayofweek from timetable,subjects where subjects.subjectcode=timetable.subjectcode and timetable.slot='12Noon-1Pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester=" + self.cb2.get() + " and dayofweek='" + day + "'"

            self.cr.execute(s)

            ans = self.cr.fetchone()
            if ans != None:
                slot3.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot3.append("Free Lecture")

            print(slot3)

        self.t1.insert("", index=2, values=slot3)


        slot4 = ["1Pm-2Pm"]
        for day in days:
            s = "select timetable.teachername,timetable.subjectcode,subjects.subjectname,timetable.dayofweek from timetable,subjects where subjects.subjectcode=timetable.subjectcode and timetable.slot='1Pm-2Pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester=" + self.cb2.get() + " and dayofweek='" + day + "'"

            self.cr.execute(s)

            ans = self.cr.fetchone()
            if ans != None:
                slot4.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot4.append("--BREAK--")

            print(slot4)

        self.t1.insert("", index=3, values=slot4)
        slot5 = ["2Pm-3Pm"]

        for day in days:
            s = "select timetable.teachername,timetable.subjectcode,subjects.subjectname,timetable.dayofweek from timetable,subjects where subjects.subjectcode=timetable.subjectcode and timetable.slot='2Pm-3Pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester=" + self.cb2.get() + " and dayofweek='" + day + "'"

            self.cr.execute(s)

            ans = self.cr.fetchone()
            if ans != None:
                slot5.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot5.append("Free Lecture")

            print(slot5)

        self.t1.insert("", index=4, values=slot5)
        slot6 = ["3Pm-4Pm"]

        for day in days:
            s = "select timetable.teachername,timetable.subjectcode,subjects.subjectname,timetable.dayofweek from timetable,subjects where subjects.subjectcode=timetable.subjectcode and timetable.slot='3Pm-4Pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester=" + self.cb2.get() + " and dayofweek='" + day + "'"

            self.cr.execute(s)

            ans = self.cr.fetchone()
            if ans != None:
                slot6.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot6.append("Free Lecture")

            print(slot6)

        self.t1.insert("", index=5, values=slot6)

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

        self.t1=Treeview(self.p2,columns=("slot","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"))

        self.t1.heading("slot",text="Slot Name")
        self.t1.heading("Monday",text="Monday")
        self.t1.heading("Tuesday",text="Tuesday")
        self.t1.heading("Wednesday",text="Wednesday")
        self.t1.heading("Thursday",text="Thursday")
        self.t1.heading("Friday",text="Friday")
        self.t1.heading("Saturday",text="Saturday")

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

