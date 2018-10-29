#-*-coding:utf-8-*-
import threading as td

def thread_job():
    print("this is an added thread,number is %s"%td.current_thread())

def main():
    td1=td.Thread(target=thread_job)       #添加一个新的线程
    print(td.active_count())    #显示激活线程的数量
    print(td.enumerate())       #显示线程的名称
    print(td.current_thread())  #显示当前运行的线程
    td1.start()                 #开始运行这一线程
    
    
if __name__=='__main__':
    main()
    
#每一个thread就是python的一个功能