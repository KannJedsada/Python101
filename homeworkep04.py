from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import csv

########################################################

gui = Tk()
gui.title('Home work Ep04')
gui.geometry('600x400')

########################################################

def writecsv(datalist):
    with open('data01.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data01.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        date = list(fr)
    return data

data = readcsv
##########################################################

l1 = Label(gui,text = 'บันทึกน้ำหนักนักกีฬา' ,font=('AngsanaNew',20),fg='red')
l1.pack()

lf1 = ttk.LabelFrame(gui,text = 'ชื่อนักกีฬา')
lf1.place(x=180,y=50)
lf2 = ttk.LabelFrame(gui,text='น้ำหนัก')
lf2.place(x=180,y=150)

v_data = StringVar()
w_data = StringVar()
e1 = ttk.Entry(lf1,textvariable=v_data,font=('Angsana New',25))
e1.pack(padx=10,pady=10)
e2 = ttk.Entry(lf2,textvariable=w_data,font=('Angsana New',25))
e2.pack(padx=10,pady=10)

##########################################################

def Savedata():
    t = datetime.now().strftime('วันที่ %d เดือน %m เวลา %H:%M:%S')
    name = v_data.get()
    data = w_data.get()
    text = [t, ' ชื่อ '+name ,data + ' กก.']
    writecsv(text)
    v_data.set('')
    w_data.set('')

lf3 = ttk.LabelFrame(gui)
lf3.place(x=240,y=250)
b1 = ttk.Button(lf3,text = 'บันทึก' ,command=Savedata)
b1.pack(ipadx=20,ipady=20)

gui.mainloop()