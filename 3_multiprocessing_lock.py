#-*-coding:utf-8-*-
import multiprocessing as mp
import time

def job(v,n,l):
    l.acquire()     #锁住进程
    for _ in range(10):
        time.sleep(0.1)
        v.value+=n             #取共享内存时必须使用.value
        print(v.value)
    l.release()     #释放进程
    
def multicore():
    l=mp.Lock()
    v=mp.Value('i',0)          #定义共享数据
    p1=mp.Process(target=job,args=(v,1,l))     #定义两个进程，使用共享数据,若没有lock，则两个进程会争夺共享数据
    p2=mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
if __name__=='__main__':
    multicore()