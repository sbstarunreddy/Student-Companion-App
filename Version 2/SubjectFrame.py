from libraries import *

class subjectFrame:
    def __init__(self,frames,subUtil,frameUtil):
        self.frames = frames
        self.subUtil = subUtil
        self.frameUtil = frameUtil

    def startSubjectFrame(self):
        tk.Button(self.frames.subjectFrame,text="Home",command = self.frameUtil.moveToMenu).grid(row=0,column = 0)

        label1 = ttk.Label(self.frames.subjectFrame,text="My Books/Papers Collection").grid(row = 0,column = 1,columnspan = 4)

        yscroll1 = ttk.Scrollbar(self.frames.subjectFrame)
        yscroll2 = ttk.Scrollbar(self.frames.subjectFrame)
        xscroll1 = ttk.Scrollbar(self.frames.subjectFrame,orient = tk.HORIZONTAL)

        sidemenu = ttk.Treeview(self.frames.subjectFrame,columns = ('Subjects'))
        sidemenu.grid(row=1,column = 0)

        sidemenu.column('#0',width=0)
        sidemenu.column("Subjects",anchor=CENTER, width=80,stretch=True)
        sidemenu.heading("#0",text="",anchor=CENTER)
        sidemenu.heading("Subjects",text="Subjects",anchor=CENTER)

        with open("Books.txt",'r') as bookFile:
                reader = csv.reader(bookFile)
                subjects = []
                for row in reader:
                        subjects.append(row[2])
                subjects = list(set(subjects))
                for i in subjects:
                    sidemenu.insert(parent='',index='end',text='',values=(i))

        sep1 = ttk.Separator(self.frames.subjectFrame).grid(row = 1,column = 1)

        table = ttk.Treeview(self.frames.subjectFrame,columns = ('book/paper','author','subject','location'),yscrollcommand = yscroll2.set(0,0),xscrollcommand = xscroll1.set(0,0))
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
        book = ttk.Entry(self.frames.subjectFrame,textvariable = book_entry)
        book.grid(row =2,column = 1)

        author_entry = tk.StringVar()
        author = ttk.Entry(self.frames.subjectFrame,textvariable = author_entry)
        author.grid(row=2,column = 2)

        subject_entry = tk.StringVar()
        subject = ttk.Entry(self.frames.subjectFrame,textvariable = subject_entry)
        subject.grid(row = 2,column = 3)

        location_entry = tk.StringVar()
        location = ttk.Entry(self.frames.subjectFrame,textvariable = location_entry)
        location.grid(row = 2,column = 4)

        add_entry = partial(self.subUtil.entry_addition,[book_entry,author_entry,subject_entry,location_entry,table,sidemenu])
        addentrybutton = ttk.Button(self.frames.subjectFrame,text="Add Entry",command = add_entry)
        addentrybutton.grid(row=2,column = 0)      
