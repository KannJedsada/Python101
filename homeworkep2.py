from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
gui = Tk()
gui.configure(bg='#DCFFDC')
gui.title('lnwza007')
gui.geometry('500x300')

l1 = Label(gui,text = 'กินอะไรดี' ,font = ('RSU',20),fg='black',bg='#DCFFDC')
l1.pack()

rice = ['กะเพรา','ข้าวผัด','ข้าวไข่เจียว','คะน้า']
noodles = ['ก๋วยเตี๋ยว','มาม่า','ราเมง']
drink = ['coke','pepsi','juice']

def Button1():
    text = random.choice(rice)
    messagebox.showinfo('Rice',text)
fb1 = Frame(gui)
fb1.place(x=190,y=50)
b1 = ttk.Button(fb1,text = 'ข้าว',command=Button1)
b1.pack(ipadx=20,ipady=20)

def Button2():
    text = random.choice(noodles)
    messagebox.showinfo('Noodles',text)
fb1 = Frame(gui)
fb1.place(x=190,y=130)
b1 = ttk.Button(fb1,text = 'อาหารเส้น',command=Button2)
b1.pack(ipadx=20,ipady=20)

def Button3():
    text = random.choice(drink)
    messagebox.showinfo('Drink',text)
fb1 = Frame(gui)
fb1.place(x=190,y=210)
b1 = ttk.Button(fb1,text = 'เครื่องดื่ม',command=Button3)
b1.pack(ipadx=20,ipady=20)
