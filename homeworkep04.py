from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import csv

gui = Tk()
gui.title('Home work Ep04')
gui.geometry('600x400')

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        date = list(fr)
    return data

data = readcsv

l1 = Label(gui,text = 'บันทึกน้ำหนักนักกีฬา' ,font=('AngsanaNew',20),fg='red')
l1.pack()

lf1 = ttk.LabelFrame(gui,text = 'น้ำหนัก')
lf1.place(x=150,y=50)

v_data = StringVar()
e1 = ttk.Entry(lf1,textvariable=v_data,font=('Angsana New',25))
e1.pack(padx=10,pady=10)

def Savedata():
    t = datetime.now().strftime('วันที่ %d เดือน %m เวลา %H:%M:%S')
    data = v_data.get()
    text = [t,  data + ' กก.']
    writecsv(text)
    v_data.set('')

b1 = ttk.Button(lf1,text = 'บันทึก' ,command=Savedata)
b1.pack(ipadx=20,ipady=20)

gui.mainloop()