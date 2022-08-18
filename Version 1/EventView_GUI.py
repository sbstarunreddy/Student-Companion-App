import tkinter as tk
import csv
import sys
import os.path
from tkinter import messagebox
from PIL import Image,ImageTk
from Calendar_GUI import Calendar
from CalendarView_GUI import CalendarView

root = tk.Tk()
root.title("Student Companion App")
root.resizable(True,True)

username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()

def setup():
	
	file_exists = os.path.isfile("users.txt")
	if file_exists:
		pass
	else:
		file = open("users.txt", "w+")
		file.close()
	file_exists = os.path.isfile("Events.txt")
	if file_exists:
		pass
	else:
		file = open("Events.txt", "w+")
		file.close()
def raiseFrame(frame):
	frame.tkraise()
def moveToReg():
	raiseFrame(regFrame)
def moveToLogin():
	raiseFrame(start)
def moveToBook():
	raiseFrame(createevent)
	
def moveToUser():
	raiseFrame(userFrame)
def register():
	entries = []
	with open ("users.txt",'a',newline="") as userFile:
		writer = csv.writer(userFile)
		writeList = [name.get(),username.get(),password.get()]
		writer.writerow(writeList)
		userFile.close()
	
	username.set("")
	password.set("")
	raiseFrame(start)
	
def createEvent(calendarViewFrame):
	
	date = str(datePickercalendar.day_selected)+"/"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	
	minutesString=str(minutes.get())
	if minutes.get()==0:
		minutesString = "00"
	time = str(hours.get())+":"+minutesString
	with open ("Events.txt",'a',newline="") as appFile:
		writer = csv.writer(appFile)
		writeList = [name.get(),date,time]
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
		
			if len(row)>0:
				if username.get()==row[1] and password.get()==row[2]:
					print(row[0]+" has logged in!")
					
					loggedInLabel.set("Welcome, "+row[0])
					
					global calendarViewFrame
					calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="lightblue")
					calendarViewFrame.grid(row=2, column=1, columnspan=5)
					viewCalendar = CalendarView(calendarViewFrame, {row[0]})
					name.set(row[0])
					raiseFrame(userFrame)
					
def logOut():
	
	name.set("")
	username.set("")
	password.set("")
	raiseFrame(start)

setup()

start = tk.Frame(root)
regFrame = tk.Frame(root)
userFrame = tk.Frame(root)
createevent = tk.Frame(root)
frameList=[start,regFrame,userFrame,createevent]

for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='lightblue')
	

companionimage = Image.open("studentcompanion.png")
companionImg = ImageTk.PhotoImage(companionimage ) 

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

tk.Entry(start,textvariable=username,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
tk.Entry(start,textvariable=password,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)

tk.Entry(regFrame,textvariable=name,font=("Courier", 22),bg='lightblue').grid(row=2,column=2)
tk.Entry(regFrame,textvariable=username,font=("Courier", 22),bg='lightblue').grid(row=3,column=2)
tk.Entry(regFrame,textvariable=password,font=("Courier", 22),bg='lightblue').grid(row=4,column=2)

tk.Button(start,font=("Courier", 22),bg='cyan',text="Login",command=login).grid(row=4,column=2)
tk.Button(start,font=("Courier", 22),bg='cyan',text="Register",command=moveToReg).grid(row=4,column=1)

tk.Button(regFrame,font=("Courier", 22),bg='cyan',text="Register",command=register).grid(row=5,column=2)
tk.Button(regFrame,font=("Courier", 22),bg='cyan',text="Back",command=moveToLogin).grid(row=5,column=1)

tk.Button(userFrame,font=("Courier", 22),bg='cyan',text="Log Out",command=logOut).grid(row=3,column=1)
tk.Button(userFrame,font=("Courier", 22),bg='cyan',text="Create Event",command=moveToBook).grid(row=3,column=2)

tk.Button(createevent,font=("Courier", 22),bg='cyan',text="Create Event",command=lambda :createEvent(calendarViewFrame)).grid(row=5,column=2)
tk.Button(createevent,font=("Courier", 22),bg='cyan',text="Back",command=moveToUser).grid(row=5,column=1)



timeSelectFrame = tk.Frame(createevent,borderwidth=5,bg="lightblue")
timeSelectFrame.grid(row=3,column=2)
tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="lightblue",width=2,textvariable=hours).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="lightblue").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,width=2,textvariable=minutes,values=(0,15,30,45),bg="lightblue").grid(row=1,column=3)

calendarFrame = tk.Frame(createevent, borderwidth=5, bg="lightblue")
calendarFrame.grid(row=2, column=2, columnspan=5)
datePickercalendar = Calendar(calendarFrame, {})

raiseFrame(start)
root.mainloop()
