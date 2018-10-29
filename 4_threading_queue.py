#-*-coding:utf-8-*-
import threading as td
import time
from queue import Queue

def job(l,q):                   #l是一个数组
    for i in range(len(l)):
        l[i]=l[i]**2            #求元素的平方
    q.put(l)                    #将得到的结果放入队列

def multi():
    q=Queue()                   #定义一个队列，代替原来的return，存放结果
    threads=[]                  #存放各个线程
    data=[[1,2,3],[3,4,5],[5,6,7],[3,8,9]]
    for i in range(4):          #定义4个线程
        t=td.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)       #将4个线程全都放入threads
    for thread in threads:      #给4个线程都添加join
        thread.join()
    result=[]
    for _ in range(4):          #取出队列中的值
        result.append(q.get())
    print(result)
        
if __name__=='__main__':
    multi()
    
#队列方法，put();get();