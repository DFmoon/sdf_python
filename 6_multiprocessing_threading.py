#-*- coding:utf-8 -*-
import multiprocessing as mp
import threading as td
import time

def job(q):         #定义一个函数，job不能有返回值，只能将计算结果存入队列，除非使用pool进程池
    res=0
    for i in range(1000000):    #range的范围是[0,99999]
        res+=i+2*i
    q.put(res)

def multicore():     #定义一个多核的进程模块
    q=mp.Queue()     #定义一个存放进程的队列，即进程运算完后结果放入队列
    p1=mp.Process(target=job,args=(q,)) #注意只有一个参数时必须加逗号，表明可迭代
    p2=mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()       #join的功能是等td1线程完成之后才会执行以下的语句
    p2.join()
    res1=q.get()
    res2=q.get()
    print('core:',res1+res2)
    
def normal():       #定义一个正常的模块
    res=0
    for _ in range(2):
        for i in range(1000000):
            res+=i+2*i
    print('normal:',res)

def multithread():  #定义一个线程模块
    q=mp.Queue()    #定义一个存放进程的队列，即进程运算完后结果放入队列
    t1=td.Thread(target=job,args=(q,)) #注意只有一个参数时必须加逗号，表明可迭代
    t2=td.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1=q.get()
    res2=q.get()
    print('thread:',res1+res2)
    
if __name__=='__main__':
    st=time.time()
    normal()
    st1=time.time()
    print('normal time:',st1-st)
    multithread()
    st2=time.time()
    print('multithread time:',st2-st1)
    multicore()
    st3=time.time()
    print('multicore time:',st3-st2)

#根据比较结果可知，多线程使用的时间最多，多进程使用的时间最少