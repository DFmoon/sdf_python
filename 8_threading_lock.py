#-*-coding:utf-8-*-
import threading as td

def job1():
    global A,l
    l.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    l.release()
    
def job2():
    global A,l
    l.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    l.release()
    
if __name__=='__main__':
    l=td.Lock()
    A=0
    t1=td.Thread(target=job1)
    t2=td.Thread(target=job2)
    t1.start()      #故意打乱顺序，测试threading的lock
    t2.start()
    t1.join()
    t2.join()