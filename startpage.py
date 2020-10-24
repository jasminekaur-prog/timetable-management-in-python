
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

import two
import viewsubjects
import AddTimetable
import showtimetable
import managecourses
import viewcourse
import editdeleteprogram
import editdeletesubjects
import edittimetab



class startpage:
    def fire0(self):
        obj=managecourses.demo()
    def fire00(self):
        obj=viewcourse.demo()
    def fire01(self):
        obj=editdeleteprogram.editdelete()
    def fire1(self):
        obj=two.demo()

    def fire2(self):
        obj=viewsubjects.demo()

    def fire3(self):
        obj=AddTimetable.addtimetabele()

    def fire4(self):
        obj=showtimetable.demo()
    def fire5(self):
        obj=editdeletesubjects.demo()

    def fire6(self):
        obj=edittimetab.demo()

    def __init__(self):
        self.root=Tk()
        self.root.geometry("1800x800")

        self.mymenu = Menu(self.root)
        self.root.title("Menu Window")
        self.root.config(menu=self.mymenu)

        submenu1 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Course", menu=submenu1)
        submenu1.add_command(label="Add New Course" ,command=self.fire0)
        submenu1.add_command(label="View All Course",command=self.fire00)
        submenu1.add_command(label="Edit/Delete Courses",command=self.fire01)

        submenu2 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Subjects", menu=submenu2)
        submenu2.add_command(label="Add New Subjects",command=self.fire1)
        submenu2.add_command(label="View Subject Course Wise",command=self.fire2)
        submenu2.add_command(label="Edit/Delete Subjects",command=self.fire5)

        submenu3 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Time Table", menu=submenu3)
        submenu3.add_command(label="Add New Time Table",command=self.fire3)
        submenu3.add_command(label="View Time Table",command=self.fire4)
        submenu3.add_command(label="Edit/Delete Time Table",command=self.fire6)



        self.root.mainloop()
#-------------------------------------------------
startpage()
