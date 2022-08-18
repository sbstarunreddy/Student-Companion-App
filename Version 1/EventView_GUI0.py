import tkinter as tk
import csv
import sys
import os.path
from functools import partial
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Calendar_GUI import Calendar
from CalendarView_GUI import CalendarView

window = tk.Tk()
window.title("Student Companion App")
window.resizable(True,True)
#Tikinter Vars
username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()
#Functions
def setup():
	#User List
	file_exists = os.path.isfile("users.txt")
	if file_exists:
		pass
	else:
		file = open("users.txt", "w+")
		file.close()

	#User-Event List
	file_exists = os.path.isfile("Events.txt")
	if file_exists:
		pass
	else:
		file = open("Events.txt", "w+")
		file.close()

	#User-Books-Papers List	
	file_exists = os.path.isfile("Books.txt")
	if file_exists:
		pass
	else:
		file = open("Books.txt", "w+")
		file.close()
	#User-Activities List	
	file_exists = os.path.isfile("Activities.txt")
	if file_exists:
		pass
	else:
		file = open("Activities.txt", "w+")
		file.close()

def raiseFrame(frame):
	frame.tkraise()
def moveToReg():
	raiseFrame(regFrame)
def moveToLogin():
	raiseFrame(start)
def moveToevent():
	raiseFrame(createevent)
	# Calendar
def moveToUser():
	raiseFrame(userFrame)
def moveToSubject():
    raiseFrame(subjectFrame)
def moveToMenu():
    raiseFrame(menu)
def moveToActivities():
	raiseFrame(activitiesFrame)

def register():
	entries = []
	with open ("users.txt",'a',newline="") as userFile:
		writer = csv.writer(userFile)
		writeList = [name.get(),username.get(),password.get()]
		writer.writerow(writeList)
		userFile.close()
	#Clear entry boxes
	username.set("")
	password.set("")
	raiseFrame(start)
	
def createEvent(calendarViewFrame):
	#Format date
	date = str(datePickercalendar.day_selected)+"/"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	#Format time
	minutesString=str(minutes.get())
	if minutes.get()==0:
		minutesString = "00"
	time = str(hours.get())+":"+minutesString
	with open ("Events.txt",'a',newline="") as appFile:
		writer = csv.writer(appFile)
		writeList = [name.get(),title,date,time,description]
		writer.writerow(writeList)
		appFile.close()
	messagebox.showinfo("Success!","Event Created!")
	calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="lightblue")
	calendarViewFrame.grid(row=2, column=1, columnspan=5)
	viewCalendar = CalendarView(calendarViewFrame, {name.get()})
	raiseFrame(userFrame)
	
def login():
	with open("users.txt",'r') as userFile:
		reader = csv.reader(userFile)
		for row in reader:
			#removes empty list from loop
			if len(row)>0:
				if username.get()==row[1] and password.get()==row[2]:
					print(row[0]+" has logged in!")
					#Set welcome message
					loggedInLabel.set("Welcome, "+row[0])
					
					# Calendar View
					global calendarViewFrame
					calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="lightblue")
					calendarViewFrame.grid(row=2, column=1, columnspan=5)
					viewCalendar = CalendarView(calendarViewFrame, {row[0]})
					name.set(row[0])
					raiseFrame(menu)
					#raiseFrame(userFrame)

def activity_addition(l_entry):
    activity_ID = l_entry[0].get()
    activity_Title = l_entry[1].get()
    activity_ST = l_entry[2].get()
    activity_ET = l_entry[3].get()
    activity_Des = l_entry[4].get()
    with open ("Activities.txt",'a',newline="") as ActivityFile:
            writer = csv.writer(ActivityFile)
            writeList = [activity_ID, activity_Title, activity_ST, activity_ET,	activity_Des]
            writer.writerow(writeList)
            ActivityFile.close()
    raiseFrame(activitiesFrame)

def book_addition(l_entry):
    book = l_entry[0].get()
    author = l_entry[1].get()
    subject = l_entry[2].get()
    location = l_entry[3].get()
    with open ("Books.txt",'a',newline="") as subjectFile:
            writer = csv.writer(subjectFile)
            writeList = [book,author,subject,location]
            writer.writerow(writeList)
            subjectFile.close()
    raiseFrame(subjectFrame)
    
					
def logOut():
	#Clear Entry boxes
	name.set("")
	username.set("")
	password.set("")
	raiseFrame(start)
#Call setup
setup()
#Define Frame
start = tk.Frame(window)
menu = tk.Frame(window)
regFrame = tk.Frame(window)
userFrame = tk.Frame(window)
createevent = tk.Frame(window)
subjectFrame = tk.Frame(window)
activitiesFrame = tk.Frame(window)
frameList=[start, menu,regFrame,userFrame,createevent,subjectFrame, activitiesFrame]
#Configure all (main) Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='lightblue')
	
#Define Image
companionimage = Image.open("studentcompanion.png")
companionImg = ImageTk.PhotoImage(companionimage ) 
#Labels
tk.Label(start,text="Student Companion App",font=("Courier", 60),bg='lightblue').grid(row=0,column=1,columnspan=5)
tk.Label(start,image=companionImg,bg='lightblue').grid(row=1,column=1,columnspan=5)
tk.Label(start,text="Username: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
tk.Label(start,text="Password: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)

tk.Label(regFrame,text="Register",font=("Courier", 44),bg='lightblue').grid(row=1,column=1,columnspan=5)
tk.Label(regFrame,text="Name: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
tk.Label(regFrame,text="Username: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
tk.Label(regFrame,text="Password: ",font=("Courier", 22),bg='lightblue').grid(row=4,column=1)

tk.Label(userFrame,textvariable = loggedInLabel,font=("Courier", 44),bg='lightblue',fg="blue").grid(row=1,column=1,columnspan=5)

tk.Label(createevent,text="Create an Event",font=("Courier", 44),bg='lightblue').grid(row=1,column=1,columnspan=5)
tk.Label(createevent,text="Select a Date: ",font=("Courier", 22),bg='lightblue').grid(row=2,column=1)
tk.Label(createevent,text="Select a Time: ",font=("Courier", 22),bg='lightblue').grid(row=3,column=1)
#Entry Boxes
tk.Entry(start,textvariable=username,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
tk.Entry(start,textvariable=password,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)

tk.Entry(regFrame,textvariable=name,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
tk.Entry(regFrame,textvariable=username,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)
tk.Entry(regFrame,textvariable=password,font=("Courier", 22),bg='lightblue').grid(row=4,column=2)
#Buttons
tk.Button(start,font=("Courier", 22),bg='cyan',text="Login",command=login).grid(row=4,column=2)
tk.Button(start,font=("Courier", 22),bg='cyan',text="Register",command=moveToReg).grid(row=4,column=1)

tk.Button(regFrame,font=("Courier", 22),bg='cyan',text="Register",command=register).grid(row=5,column=2)
tk.Button(regFrame,font=("Courier", 22),bg='cyan',text="Back",command=moveToLogin).grid(row=5,column=1)

tk.Button(userFrame,font=("Courier", 22),bg='cyan',text="Events",command=moveToevent).grid(row=3,column=2)
tk.Button(userFrame,font=("Courier", 22),bg='cyan',text="Home",command = moveToMenu).grid(row=0,column = 0)
					

tk.Button(createevent,font=("Courier", 22),bg='cyan',text="Create Event",command=lambda :createEvent(calendarViewFrame)).grid(row=5,column=2)
tk.Button(createevent,font=("Courier", 22),bg='cyan',text="Back",command=moveToUser).grid(row=5,column=1)

######################################################################################################################

'''
----------------------------------------------------------------------------------------------------------------------
Beginning of menu Frame
menu : We offer two services for the user. A calendar to keep track of date and add events and a
place to store details of all his/her learning resouces. Once the user logs in, he is directed to
this menu frame where he choses the activity he wants to perform.
'''

tk.Label(menu,textvariable = loggedInLabel,font=("Courier", 44),bg='lightblue',fg="blue").grid(row=1,column=1,columnspan=5)

goToCalendar = tk.Button(menu,font=("Courier", 22),bg='cyan',text="Calendar",command = moveToUser).grid(row = 4, column = 3)

goToPapers = tk.Button(menu,font=("Courier", 22),bg='cyan',text="Books and Papers",command = moveToSubject).grid(row = 4, column = 4)

goToActivities = tk.Button(menu,font=("Courier", 22),bg='cyan',text="Activities",command = moveToActivities).grid(row = 4, column = 5)

menuLogOut = tk.Button(menu,font=("Courier", 22),bg='cyan', text = "Log Out",command = logOut).grid(row = 6, column = 0)

sep1 = ttk.Separator(menu).grid(row = 2,column = 0,columnspan = 6)

'''
End of menu Frame
--------------------------------------------------------------------------------------------------------------------
'''

######################################################################################################################

'''
---------------------------------------------------------------------------------------------------------------------
Beginning of subjectFrame
subjectFrame : This is the frame where the user can view all the learning resources.
He/she can also add a new learning resource in this frame.
'''

tk.Button(subjectFrame,font=("Courier", 22),bg='cyan',text="Home",command = moveToMenu).grid(row=0,column = 0)


label1 = ttk.Label(subjectFrame,text="My Books/Papers Collection").grid(row = 0,column = 1,columnspan = 4)

yscroll1 = ttk.Scrollbar(subjectFrame)
yscroll2 = ttk.Scrollbar(subjectFrame)
xscroll1 = ttk.Scrollbar(subjectFrame,orient = tk.HORIZONTAL)

sidemenu = ttk.Treeview(subjectFrame,columns = ('Subjects'))
sidemenu.grid(row=1,column = 0)

sidemenu.column('#0',width=0)
sidemenu.column("Subjects",anchor=CENTER, width=80,stretch=True)
sidemenu.heading("#0",text="",anchor=CENTER)
sidemenu.heading("Subjects",text="Subjects",anchor=CENTER)

sep1 = ttk.Separator(subjectFrame).grid(row = 1,column = 1)

table = ttk.Treeview(subjectFrame,columns = ('book/paper','author','subject','location'),yscrollcommand = yscroll2.set(0,0),xscrollcommand = xscroll1.set(0,0))
table.grid(row=1,column = 1,columnspan = 4)

table.column("#0", width=0)
table.column("book/paper",anchor=CENTER, width=150,stretch=True)
table.column("author",anchor=CENTER,width=150,stretch=True)
table.column("subject",anchor=CENTER,width=150,stretch=True)
table.column("location",anchor=CENTER,width=150,stretch=True)

table.heading("#0",text="",anchor=CENTER)
table.heading("book/paper",text="Title",anchor=CENTER)
table.heading("author",text="Author",anchor=CENTER)
table.heading("subject",text="Subject",anchor=CENTER)
table.heading("location",text="Location",anchor=CENTER)

with open("Books.txt",'r') as bookFile:
        reader = csv.reader(bookFile)
        for row in reader:
                table.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3]))

book_entry = tk.StringVar()
book = ttk.Entry(subjectFrame,textvariable = book_entry)
book.grid(row =2,column = 1)

author_entry = tk.StringVar()
author = ttk.Entry(subjectFrame,textvariable = author_entry)
author.grid(row=2,column = 2)

subject_entry = tk.StringVar()
subject = ttk.Entry(subjectFrame,textvariable = subject_entry)
subject.grid(row = 2,column = 3)

location_entry = tk.StringVar()
location = ttk.Entry(subjectFrame,textvariable = location_entry)
location.grid(row = 2,column = 4)

add_entry = partial(book_addition,[book_entry,author_entry,subject_entry,location_entry])
addentrybutton = ttk.Button(subjectFrame,text="Add Entry",command = add_entry)
addentrybutton.grid(row=2,column = 0)

'''
End of subjectFrame
---------------------------------------------------------------------------------------------------------------------
'''

#####################################################################################################################

'''
---------------------------------------------------------------------------------------------------------------------
Beginning of actvitiesFrame
subjectFrame : This is the frame where the user can view all the learning resources.
He/she can also add a new learning resource in this frame.
'''

tk.Button(activitiesFrame,font=("Courier", 22),bg='cyan',text="Home",command = moveToMenu).grid(row=0,column = 0)


label1 = ttk.Label(activitiesFrame,text="My Planned Activities").grid(row = 0,column = 1,columnspan = 2)

yscroll1 = ttk.Scrollbar(activitiesFrame)
yscroll2 = ttk.Scrollbar(activitiesFrame)
xscroll1 = ttk.Scrollbar(activitiesFrame,orient = tk.HORIZONTAL)

sidemenu = ttk.Treeview(activitiesFrame,columns = ('Activities'))
sidemenu.grid(row=1,column = 0)

sidemenu.column('#0',width=0)
sidemenu.column("Activities",anchor=CENTER, width=100,stretch=True)
sidemenu.heading("#0",text="",anchor=CENTER)
sidemenu.heading("Activities",text="Activities",anchor=CENTER)

sep1 = ttk.Separator(activitiesFrame).grid(row = 1,column = 1)

table = ttk.Treeview(activitiesFrame,columns = ('ID','Name','Start Time','End Time','Description'),yscrollcommand = yscroll2.set(0,0),xscrollcommand = xscroll1.set(0,0))
table.grid(row=1,column = 1,columnspan = 5)

table.column("#0", width=0)
table.column("ID",anchor=CENTER, width=150,stretch=True)
table.column("Name",anchor=CENTER,width=150,stretch=True)
table.column("Start Time",anchor=CENTER,width=150,stretch=True)
table.column("End Time",anchor=CENTER,width=150,stretch=True)
table.column("Description",anchor=CENTER,width=350,stretch=True)

table.heading("#0",text="",anchor=CENTER)
table.heading("ID",text="ID",anchor=CENTER)
table.heading("Name",text="Name",anchor=CENTER)
table.heading("Start Time",text="Start Time",anchor=CENTER)
table.heading("End Time",text="End Time",anchor=CENTER)
table.heading("Description",text="Description",anchor=CENTER)

with open("Activities.txt",'r') as ActivityFile:
        reader = csv.reader(ActivityFile)
        for row in reader:
                table.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4]))

ID_entry = tk.StringVar()
ID = ttk.Entry(activitiesFrame,textvariable = ID_entry)
ID.grid(row =2,column = 1)

Name_entry = tk.StringVar()
Name = ttk.Entry(activitiesFrame,textvariable = Name_entry)
Name.grid(row=2,column = 2)

ST_entry = tk.StringVar()
ST = ttk.Entry(activitiesFrame,textvariable = ST_entry)
ST.grid(row = 2,column = 3)

ET_entry = tk.StringVar()
ET = ttk.Entry(activitiesFrame,textvariable = ET_entry)
ET.grid(row = 2,column = 4)

Des_entry = tk.StringVar()
Des = ttk.Entry(activitiesFrame,textvariable = Des_entry)
Des.grid(row = 2,column = 5)


add_entry = partial(activity_addition,[ID_entry,Name_entry,ST_entry,ET_entry,Des_entry])
addentrybutton = ttk.Button(activitiesFrame,text="Add Entry",command = add_entry)
addentrybutton.grid(row=2,column = 0)

'''
End of subjectFrame
---------------------------------------------------------------------------------------------------------------------
'''
######################################################################################################################



#Time Selector
timeSelectFrame = tk.Frame(createevent,borderwidth=5,bg="lightblue")
timeSelectFrame.grid(row=3,column=2)
tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="lightblue",width=2,textvariable=hours).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="lightblue").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,width=2,textvariable=minutes,values=(0,15,30,45),bg="lightblue").grid(row=1,column=3)

calendarFrame = tk.Frame(createevent, borderwidth=5, bg="lightblue")
calendarFrame.grid(row=2, column=2, columnspan=5)
datePickercalendar = Calendar(calendarFrame, {})
#Raise Initial Frame
raiseFrame(start)
window.mainloop()
