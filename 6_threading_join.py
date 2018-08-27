#-*-coding:utf-8-*-
import threading as td
import time

def thread_job():
    print("td1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("td1 finish\n")
    
def main():
    td1=td.Thread(target=thread_job,name='td1') #添加一个新的线程，name属性用于为添加的线程命名
    td1.start()
    td1.join()      #join的功能是等td1线程完成之后才会执行以下的语句
    print("all done")
    
if __name__=='__main__':
    main()