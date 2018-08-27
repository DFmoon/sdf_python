#-*- coding:utf-8 -*-
import multiprocessing as mp

def job(x):             #job可以有返回值
    return x*x

def multicore():
    pool=mp.Pool(processes=3)      #定义一个进程池，默认将分配给所有的核，也可以传参自定义使用的核的数量
    res=pool.map(job,range(10))    #在进程池中放入方程和需要运算的值后，map会自动分配给每一个核，并返回
    print(res)
    res=pool.apply_async(job,(2,)) #apply_async只能一次在一个进程中算一个东西
    print(res.get())
    multi_res=[pool.apply_async(job,(i,))for i in range(10)]  #可以使用迭代器实现map的功能
    print([res.get() for res in multi_res])    #在列表中迭代输出
    
if __name__=='__main__':
    multicore()