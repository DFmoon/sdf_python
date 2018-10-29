#-*-coding:utf-8-*-
import numpy as np

array=np.array([[1,2,3],[2,3,4]],dtype=np.int64)   #将数组转化为矩阵，dtype=np.int64表示元素的类型
print(array)                            #打印矩阵
print(array.dtype)                      #元素类型
print('number of dim:',array.ndim)      #数组维数
print('shape:',array.shape)             #行数和列数
print('size:',array.size)               #元素个数

#生成矩阵***************************************************************************************
a1=np.zeros((3,4))     #生成全0矩阵，注意双层括号
print('a1:\n',a1)

a2=np.ones((3,4))      #生成全1矩阵
print('a2:\n',a2)

a3=np.empty((4,4))     #生成空矩阵，实际上生成的是数值很小的矩阵
print('a3:\n',a3)

a4=np.arange(10,20,2)  #生成有序数列，范围在10-20，步长为2
print('a4:\n',a4)

a5=np.arange(12).reshape((3,4))         #生成有序数列，reshape((3,4))指定行数和列数
print('a5:\n',a5)

a6=np.linspace(1,10,6).reshape((2,3))   #生成范围在1和10及其之间的6个数，重定行数和列数[[ 1.   2.8  4.6][ 6.4  8.2 10. ]]
print('a6:\n',a6)

a7=np.random.random((4,3))              #随机生成0-1的矩阵
print('a7:\n',a7)

#运算*****************************************************************************************
#减法
b=a5-a2
print('b:\n',b)
#加法
c=a5+a2
print('c:\n',c)
#平方
d=a5**2
print('d:\n',d)
#求sin
e=np.sin(a5)
print('e:\n',e)
#求cos
f=np.cos(a5)
print('f:\n',f)
#求tan
g=np.tan(a5)
print('g:\n',g)
#打印是否小于3的元素结果(其他比较符都适用)
print(a5<6)
#对应元素相乘
h=a5*a2
print('h:\n',h)
#矩阵乘法
i=np.dot(a5,a3)
i_the_same=a5.dot(a3)
print('i:\n',i,'\ni_the_same:\n',i_the_same)
#求和，最值，平均值，中位数，累加，累差
print('a5中所有元素和是：',np.sum(a5))          #a5.sum()的形式也可
print('a5中的最小值是：',np.min(a5))
print('a5中的最大值是：',np.max(a5))
print('a5中所有元素平均值是：',np.mean(a5))
print('a5中所有元素平均值是：',np.average(a5))   #average不能使用a5.sum()的形式
print('a5的中位数是：',np.median(a5))
print('a5元素逐步累加可得：',np.cumsum(a5))
print('a5元素逐步累差可得：\n',np.diff(a5))
print('a5中每列元素和是：',np.sum(a5,axis=0))    #axis=0表示每一列运算，axis=1表示每一行运算
print('a5中每行元素最小值是：',np.min(a5,axis=1))
print('a5中每列元素最大值是：',np.max(a5,axis=0))
print('a5中每行元素平均值是：',np.mean(a5,axis=1))
#判断元素
print('a5中非零元素是：\n',np.nonzero(a5)) #返回两个数组，第一个数组为非零元素的行，第二个数组为非零元素的列
#排序
print('a7逐行排序可得：\n',np.sort(a7))    #每一行各自进行排序
#矩阵转置
print('a5的转置矩阵为：\n',np.transpose(a5))
print('a5的转置矩阵为：\n',a5.T)
#求索引
print('a5中的最小值索引是：',np.argmin(a5))
print('a5中的最大值索引是：',np.argmax(a5))
#截断
print('a5仅范围5-9截断可得：\n',np.clip(a5,5,9))    #所有小于5的数都等于5，所有大于9的数都等于9