#-*-coding:utf-8-*-
import tkinter as tk

win=tk.Tk()
win.title('sdf')
win.geometry('400x400')

canvas=tk.Canvas(win,bg='pink',height=200,width=400)    #创建一个画布
image_file=tk.PhotoImage(file='1.gif')                  #获取图片文件
image=canvas.create_image(0,0,anchor='nw',image=image_file) #在画布上载入图片

x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)                    #画线
oval=canvas.create_oval(x0+30,y0+30,x1+30,y1+30,fill='yellow')      #画圆
arc=canvas.create_arc(x0+60,y0+60,x1+60,y1+60,start=90,extent=180,fill='blue')      #画扇形
rect=canvas.create_rectangle(100,30,120,50,fill='red')  #画方形
canvas.pack()

def moveit():           #点击按钮，移动画布中的方形
    canvas.move(rect,0,2)
    
b=tk.Button(win,text='move',command=moveit)
b.pack()


win.mainloop()      #不断循环刷新