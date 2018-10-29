#-*-coding:utf-8-*-
import tkinter as tk

win=tk.Tk()
win.title('sdf')
win.geometry('200x200')

#pack********************************************************************************
'''tk.Label(win,text=1,bg='pink').pack(side='top')
tk.Label(win,text=1,bg='pink').pack(side='bottom')
tk.Label(win,text=1,bg='pink').pack(side='left')
tk.Label(win,text=1,bg='pink').pack(side='right')'''

#grid********************************************************************************
'''for i in range(4):
    for j in range(3):
        tk.Label(win,text=2,bg='yellow').grid(row=i,column=j,padx=10,pady=10,ipadx=10,ipady=10)'''
        #grid将win划分成网格，padx=10,pady=10表示x和y方向的margin,ipadx=10,ipady=10表示x和y方向的padding

#place*******************************************************************************
tk.Label(win,text=3,bg='blue').place(x=10,y=100,anchor='nw')    #定点放置

win.mainloop()