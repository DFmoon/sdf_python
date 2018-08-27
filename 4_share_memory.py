#-*-coding:utf-8-*-
import multiprocessing as mp

value=mp.Value('i',0)    #i表示共享的数据是整数类型，该数据可供所有核使用修改
array=mp.Array('i',[2,3,1,4])       #此处的数组只能是一维的