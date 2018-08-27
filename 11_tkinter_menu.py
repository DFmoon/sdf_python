#-*-coding:utf-8-*-
import tkinter as tk

win=tk.Tk()
win.title('sdf')
win.geometry('400x400')

l=tk.Label(win,text='',bg='pink',width=20,height=2)
l.pack()

counter=0
def new_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1
menubar=tk.Menu(win)                                #窗口上创建一个菜单栏
filemenu=tk.Menu(menubar,tearoff=0)                 #在菜单栏上创建一个file按键，tearoff=0表示不能分割出来
menubar.add_cascade(label='file',menu=filemenu)     #将file添加到菜单栏中，命名为file
filemenu.add_command(label='New',command=new_job)   #给file按键添加各种功能
filemenu.add_command(label='Open',command=new_job)
filemenu.add_command(label='Save',command=new_job)
filemenu.add_separator()                            #添加分割线
filemenu.add_command(label='Exit',command=win.quit)

submenu=tk.Menu(filemenu,tearoff=0)                 #在file按键上创建一个submenu
filemenu.add_cascade(label='import',menu=submenu)   #将submenu添加到菜单栏中，命名为import
submenu.add_command(label='Sub1',command=new_job)   #给import添加功能Sub1

win.config(menu=menubar)                            #将menubar添加到窗口的menu属性中

win.mainloop()