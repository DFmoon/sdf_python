#-*-coding:utf-8-*-
import tkinter as tk
import pickle
from tkinter import messagebox

win=tk.Tk()
win.title('load')
win.geometry('450x300')

#加载图片
canvas=tk.Canvas(win,height=200,width=500)
image_file=tk.PhotoImage(file='2.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#标签和输入框
var_username=tk.StringVar()
var_username.set('example@python.com')      #设置输入框的缺省值
var_password=tk.StringVar()

tk.Label(win,text='user name',font=('Arial',16)).place(x=50,y=150)
tk.Label(win,text='password',font=('Arial',16)).place(x=50,y=190)
entry_username=tk.Entry(win,textvariable=var_username,font=('Arial',14))
entry_username.place(x=160,y=150)
entry_password=tk.Entry(win,textvariable=var_password,show='*',font=('Arial',14))
entry_password.place(x=160,y=190)

#按钮
def login():
    username=var_username.get()
    password=var_password.get()
    try:
        with open('infos.pickle','rb')as info:
            infos=pickle.load(info)
    except FileNotFoundError:
        with open('infos.pickle','wb')as info:
            infos={'admin':'admin'}
            pickle.dump(infos,info)
    if username in infos:
        if password==infos[username]:
            tk.messagebox.showinfo(title='welcome',message='how are you?'+username)
        else:
            tk.messagebox.showerror(title='error',message='password is wrong,please try again.')
    else:
        res_sign=tk.messagebox.askyesno(title='weicome',message='you have not sign up yet.sign up?')
        if res_sign:
            sign_up()
def sign_up():
    def sign_to_Mofan_Python():
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
        nn=new_name.get()
        with open('infos.pickle','rb')as info:
            exist_info=pickle.load(info)
        if np!=npf:
            tk.messagebox.showerror(title='error',message='password and confirm password must be the same')
        elif nn in exist_info:
            tk.messagebox.showerror(title='error',message='the user has aready signed up!')
        else:
            exist_info[nn]=np
            with open('infos.pickle','wb')as info:
                pickle.dump(exist_info,info)
            tk.messagebox.showinfo(title='welcome',message='sign up successfully')
            sign_up_win.destroy()
        
    sign_up_win=tk.Toplevel(win)        #在win上创建一个登陆的子窗口
    sign_up_win.geometry('350x200')
    sign_up_win.title('sign_up_win')
    
    new_name = tk.StringVar()#将输入的注册名赋值给变量
    new_name.set('example@python.com')#将最初显示定为'example@python.com'
    tk.Label(sign_up_win, text='User name: ').place(x=10, y= 10)#将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(sign_up_win, textvariable=new_name)#创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=150, y=10)#`entry`放置在坐标（150,10）.
    
    new_pwd = tk.StringVar()
    tk.Label(sign_up_win, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(sign_up_win, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)
    
    new_pwd_confirm = tk.StringVar()
    tk.Label(sign_up_win, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(sign_up_win, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)
    
    btn_comfirm_sign_up = tk.Button(sign_up_win, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)    
    

b1=tk.Button(win,text='login',command=login)
b1.place(x=150,y=230)
b2=tk.Button(win,text='sign up',command=sign_up)
b2.place(x=250,y=230)

win.mainloop()