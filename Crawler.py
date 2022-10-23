def recNestedListSumOfEvenNumbers(lst):
    if len(lst) == 0:
        return 0
    if type(lst[0]) == list:
        return recNestedListSumOfEvenNumbers(lst[0]) + recNestedListSumOfEvenNumbers(lst[1:])
    if (lst[0])% 2 == 0:
        return lst[0] + recNestedListSumOfEvenNumbers(lst[1:])
    else:
        return recNestedListSumOfEvenNumbers(lst[1:])
    return recNestedListSumOfEvenNumbers(lst[1:])
        
    
def recLetterCount(lst,letter):
    'returns a count of how many times a letter is found in the strings in a list. Case should be ignored'
    if len(lst) == 0:
        return 0

    if type(lst[0]) == str and letter.upper() in lst[0].upper():
        str_upper = lst[0].upper()
        index = str_upper.find(letter.upper())
        num_matches = 1 + recLetterCount(list(str_upper[index+1:]), letter)
        return num_matches + recLetterCount(lst[1:], letter)
    elif type(lst[0]) == list:
        return recLetterCount(lst[0], letter) + recLetterCount(lst[1:], letter)
    else:   
        return recLetterCount(lst[1:], letter)
    
    
import os

def dirPrint(pathname, indent):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    print(indent * ' ', pathname)
    for item in os.listdir(pathname):
        n = os.path.join(pathname,item)
        if os.path.isdir(n):
            dirPrint(n, indent + 2)
import os

def fileCount(pathname, fileName):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    count = 0
    
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        
        if os.path.isdir(n):
            count += fileCount(n, fileName)
        elif item == fileName:
            count += 1

    return count

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END,filedialog
from tkinter.messagebox import showinfo

###EXAMPLE############

class FileDialogExample(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('FileDialog Example')
        self.make_widgets()
    def getPath(self):
        path = filedialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        print(path)
        
    def make_widgets(self):
        Button(self, text="Print Path", command=lambda:self.getPath()).grid(column=0,row=0)

#FileDialogExample().mainloop()
####END EXAMPLE########


class FileCountExplorer(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('File Count Explorer')
        self.make_widgets()

    def getPath(self):
        path = filedialog.askdirectory(parent=self,initialdir="/",title='{} is being looked for'.format(self.Entry1.get()))
        self.Entry2.insert(0,path)  
        
    def getCount(self):
        if self.Entry1.get() == '':
            showinfo('Error.', 'You must Enter a filename.')
        if self.Entry2.get() == '' and len(self.Entry1.get()) > 0:
            showinfo('Error.', 'You must select a folder path.')
        else:
            showinfo('Total Files found', self.fileCount(self.Entry2.get(),self.Entry1.get()))


    def fileCount(self,pathname, fileName):
        count = 0
        for item in os.listdir(pathname):
            n = os.path.join(pathname, item)
        if os.path.isdir(n):
            count += fileCount(pathname, fileName)
        elif item == fileName:
            count += 1
        return count
    def make_widgets(self):
        #Labels

        Label(self, text = 'Enter a file name:').grid(row = 0, column = 0)
        Label(self, text = 'Select path:').grid(row = 1, column = 0)
        #Buttons
        
        Button(self, text = 'Get Path', command = lambda:self.getPath()).grid(row = 1, column = 2)
        Button(self, text = 'Get Count', command = lambda:self.getCount()).grid(row = 2, column = 2)

        #Entries
        self.Entry1 = Entry(self, width = 35)
        self.Entry1.grid(row = 0, column = 1)
        self.Entry2 = Entry(self, width = 35)
        self.Entry2.grid(row = 1, column = 1)

#FileCountExplorer().mainloop()

from tkinter import Label, Tk, Entry, Button, END
from tkinter.messagebox import showinfo

class CalendarItem(object):
    def __init__(self,name,date):
        self.name = name
        self.date = date

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def __str__(self):
        pass

class CalendarGUI(Tk):
    def __init__(self,parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title('Calendar GUI')
        self.filename = 'calendar.txt'
        self.make_widgets()
        self.loadCalendar()
        showinfo('Calendar', 'Calendar loaded.')

    def loadCalendar(self):
        self.items = {}
        f = open('calendar.txt', 'r')
        for line in f.readlines():
            line = line.split(':')
            self.items[line[0]] = line[1]
        self.updateLabel()
        f.close()
        

    def updateLabel(self):
        self.firstlabel.config(text = 'The calendar has {} items.'.format(len(self.items)))
    
    def saveCalendar(self):
        if self.Entry1.get() == '':
            showinfo('Event Error', 'Event must have a name.')
        elif self.Entry2.get() == '':
            showinfo('Event Error', 'Event must have a date.')
        else:
            f = open('calendar.txt', 'a')
            w = f.write(self.Entry1.get() + ':' + self.Entry2.get() + '\n')
            self.items[self.Entry1.get()] = self.Entry2.get()
            self.updateLabel()

    def find(self):
        try:
            Date = self.items[self.Entry1.get()]
            self.Entry2.insert(0, Date)
            showinfo('Calendar Item', 'Item Found')
        except:
            showinfo('Calendar Item', 'Item Not Found')
    
    def make_widgets(self):
        'defines GUI widgets'
        #Labels

        self.firstlabel = Label(self, text = 'The calendar has 0 items.')
        self.firstlabel.grid(row = 0, column = 0)
        Label(self, text = 'Event Name:').grid(row = 1, column = 0)
        Label(self, text = 'Event Date:').grid(row = 2, column = 0)
        #Buttons
        
        Button(self, text = 'Add Event', command = self.saveCalendar).grid(row = 3, column = 0)
        Button(self, text = 'Get Event Date', command = self.find).grid(row = 3, column = 1)

        #Entries
        self.Entry1 = Entry(self, width = 15)
        self.Entry1.grid(row = 1, column = 1)
        self.Entry2 = Entry(self, width = 15)
        self.Entry2.grid(row = 2, column = 1)
    
#print(recNestedListSumOfEvenNumbers([]))                               
#print(recNestedListSumOfEvenNumbers([[1,2,3,4,5,6,7,8,9,10]]))
#print(recNestedListSumOfEvenNumbers([[[[[[[[[5]]]]]]]]]))
#print(recNestedListSumOfEvenNumbers([[1,2,3],[4,[[[5,[[[6]]]]]]]]))
#print(recNestedListSumOfEvenNumbers([[[[[[[[[10,20]]]]]]]]]))

#print(recLetterCount([],'a'))
#print(recLetterCount([1,'aaa',3,4,5],'A'))
#print(recLetterCount([[[[[[1,'test test']],3]]],[['test',5.0,'test test']]],'E'))

#dirPrint('Test',2)
#dirPrint('count',5)

#print('FILE COUNT: ', fileCount('Test','a.txt'))
#print('FILE COUNT: ', fileCount('Test','File.txt'))
#print('FILE COUNT: ', fileCount('Test','file.txt'))

#CalendarGUI().mainloop()
