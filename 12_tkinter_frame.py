#-*-coding:utf-8-*-
import tkinter as tk

win=tk.Tk()
win.title('sdf')
win.geometry('300x200')

tk.Label(win,text='on the window',bg='pink',width=20,height=2).pack()

frm=tk.Frame(win).pack()    #在window上创建一个主框架
frm_l=tk.Frame(frm)         #在主框架上创建左右两个子框架
frm_l.pack(side='left')     #side='left'表示在主框架中靠左，当pack中需设置参数时，不能连写
frm_r=tk.Frame(frm)
frm_r.pack(side='right')

tk.Label(frm_l,text='on the frm_l1',bg='pink',width=20,height=2).pack()
tk.Label(frm_l,text='on the frm_l2',bg='pink',width=20,height=2).pack()
tk.Label(frm_r,text='on the frm_r',bg='pink',width=20,height=2).pack()

win.mainloop()