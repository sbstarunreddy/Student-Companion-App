from libraries import *

class subjectUtils:

    def __init__(self,subjectFrame):
        self.subjectFrame = subjectFrame

    def entry_addition(self,l_entry):
        book = l_entry[0].get()
        author = l_entry[1].get()
        subject = l_entry[2].get()
        location = l_entry[3].get()
        table = l_entry[4]
        sidemenu = l_entry[5]
        with open ("Books.txt",'a',newline="") as subjectFile:
            writer = csv.writer(subjectFile)
            writeList = [book,author,subject,location]
            writer.writerow(writeList)
            table.insert(parent='',index='end',text='',values=(book,author,subject,location))
            subjectFile.close()
        for item in sidemenu.get_children():
            sidemenu.delete(item)        
        with open("Books.txt",'r') as bookFile:
                reader = csv.reader(bookFile)
                subjects = []
                for row in reader:
                        subjects.append(row[2])
                subjects = list(set(subjects))
                for i in subjects:
                    sidemenu.insert(parent='',index='end',text='',values=(i))
