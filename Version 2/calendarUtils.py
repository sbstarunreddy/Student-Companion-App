from libraries import *
from Calendar import *

class calendarUtils:

        def __init__(self,userFrame,datePicker,minutes,hours,name):
                self.userFrame = userFrame
                self.datePickercalendar = datePicker
                self.minutes = minutes
                self.hours = hours
                self.name = name
                
        def createEvent(self,calendarViewFrame):
                #Format date
                date = str(self.datePickercalendar.day_selected)+"/"+str(self.datePickercalendar.month_selected)+"/"+str(self.datePickercalendar.year_selected)
                #Format time
                minutesString=str(self.minutes.get())
                if self.minutes.get()==0:
                        minutesString = "00"
                time = str(self.hours.get())+":"+minutesString
                with open ("Events.txt",'a',newline="") as appFile:
                        writer = csv.writer(appFile)
                        writeList = [self.name.get(),date,time]
                        writer.writerow(writeList)
                        appFile.close()
                messagebox.showinfo("Success!","Event Created!")
                calendarViewFrame = tk.Frame(self.userFrame, borderwidth=5, bg="lightblue")
                calendarViewFrame.grid(row=2, column=1, columnspan=5)
                viewCalendar = CalendarView(calendarViewFrame, {self.name.get()})
                self.userFrame.tkraise()
