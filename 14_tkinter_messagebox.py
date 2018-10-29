#-*-coding:utf-8-*-
import tkinter as tk
from tkinter import messagebox      #必须，否则会出错

win=tk.Tk()
win.title('sdf')
win.geometry('300x200')

def hit_me():
    tk.messagebox.showinfo(title='sdf',message='emmmm')                 #提示信息
    tk.messagebox.showwarning(title='sdf',message='nonono')             #弹出警告
    tk.messagebox.showerror(title='sdf',message='error')                #错误提示
    tk.messagebox.askquestion(title='sdf',message='yes or no')          #询问，返回值为yes或者no
    tk.messagebox.askyesno(title='sdf',message='true or false')         #询问，返回值为true或者false
    tk.messagebox.askokcancel(title='sdf',message='true or false')      #询问，返回值为true或者false
    tk.messagebox.askretrycancel(title='sdf',message='true or false')   #询问，返回值为true或者false
tk.Button(win,text='hit me',command=hit_me).pack()

win.mainloop()