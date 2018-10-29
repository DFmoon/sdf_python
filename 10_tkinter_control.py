#-*-coding:utf-8-*-
import tkinter as tk

win=tk.Tk()
win.title('sdf')
win.geometry('400x600')

#1*****************************************************************************************
var=tk.StringVar()      #tkinter中的字符串的变量
on_hit=False            #定义一个全局变量控制是否点击了按钮

#标签
l=tk.Label(win,textvariable=var,bg='pink',font=('Arial',12),width=15,height=1)
l.pack()

#按钮
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
b=tk.Button(win,text='hit',width=10,height=1,command=hit_me)
b.pack()

#2*****************************************************************************************
#输入框
e=tk.Entry(win,show=1)       #show='*'时输入框作为密码框显示，show='1'时无论输入什么都显示1，但实际数据并没有改变
e.pack()

#文本框
t=tk.Text(win,height=4,width=40)
t.pack()

#按钮
def insert_point():             #获取entry中的值并将其插入光标所在位置
    var1=e.get()
    t.insert('insert',var1)     #insert(1.2,var1)表示在第一行第二列插入
def insert_end():               #获取entry中的值并将其插入文本框尾部
    var2=e.get()
    t.insert('end',var2)
b1=tk.Button(win,text='insert point',width=10,height=1,command=insert_point)
b1.pack()
b2=tk.Button(win,text='insert end',width=10,height=1,command=insert_end)
b2.pack()

#3*****************************************************************************************
var4=tk.StringVar()     #定义标签中的变量
var5=tk.StringVar()     #定义列表中的变量
var5.set((11,22))

#标签，textvariable为动态文本，可以更新，和变量搭配使用
l2=tk.Label(win,textvariable=var4,bg='blue',font=('Arial',12),width=15,height=1)
l2.pack()

#按钮
def print_selection():               #在标签中显示选中的列表选项
    value=lb.get(lb.curselection())  #取出列表选中项
    var4.set(value)                  #设置标签中的变量值
b3=tk.Button(win,text='print selection',width=15,height=1,command=print_selection)
b3.pack()

#列表
lb=tk.Listbox(win,listvariable=var5,height=4)
list_items=[1,2,3,4]
for item in list_items:     #插入列表选项
    lb.insert('end',item)
lb.insert(1,'first')        #在特定位置插入列表选项
lb.insert(2,'second')
lb.delete(2)                #删除列表选项
lb.pack()

#4*****************************************************************************************
var6=tk.StringVar()

#标签，text为静态文本，可通过config设置
l3=tk.Label(win,text='empty',bg='yellow',font=('Arial',12),width=20,height=1)
l3.pack()

#按钮
def print_selection():
    l3.config(text='you have selected'+var6.get())        #config可以改变控件的属性
#单选按钮
r1=tk.Radiobutton(win,text='Option A',variable=var6,value='A',command=print_selection)  #var6=A
r1.pack()
r2=tk.Radiobutton(win,text='Option B',variable=var6,value='B',command=print_selection)  #var6=B
r2.pack()
r3=tk.Radiobutton(win,text='Option C',variable=var6,value='C',command=print_selection)  #var6=C
r3.pack()

#5*****************************************************************************************
#标签
l4=tk.Label(win,text='empty',bg='yellow',font=('Arial',12),width=15,height=1)
l4.pack()

def print_number(v):
    l4.config(text=v)
#滑块
s=tk.Scale(win,label='sdf',from_=0,to=100,orient=tk.HORIZONTAL,length=200,showvalue=0,resolution=1,
           tickinterval=20,command=print_number)    
#showvalue=0表示是否在滑块上方显示对应的值，resolution=1表示保留几位小数,tickinterval=20表示隔多长显示一个刻度
#滑块的command有默认的传入值，即滑块的值
s.pack()

#6*****************************************************************************************
var7=tk.IntVar()
var8=tk.IntVar()
l5=tk.Label(win,text='empty',bg='yellow',font=('Arial',12),width=15,height=1)
l5.pack()

def pring_choose():
    if(var7.get()==1)&(var8.get()==0):
        l5.config(text='I like only python')
    elif(var7.get()==0)&(var8.get()==1):
        l5.config(text='I like only c++')
    elif(var7.get()==0)&(var8.get()==0):
        l5.config(text='I do not like either')
    else:
        l5.config(text='I like both')
#复选框
c1=tk.Checkbutton(win,text='python',variable=var7,onvalue=1,offvalue=0,command=pring_choose)
#variable=var7,onvalue=1,offvalue=0表示选中时var7的值为1，不选中时为0
c1.pack()
c2=tk.Checkbutton(win,text='c++',variable=var8,onvalue=1,offvalue=0,command=pring_choose)
c2.pack()

win.mainloop()      #不断循环刷新