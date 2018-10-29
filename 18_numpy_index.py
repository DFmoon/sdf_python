#-*-coding:utf-8-*-
import numpy as np

#一维
a1=np.arange(3,15)
print(a1)
print(a1[3])

#二维
a2=np.arange(3,15).reshape((3,4))
print(a2)
print(a2[2])
print(a2[2,:])
print(a2[2,1:3])
print(a2[:,1])
print(a2[2][3])
print(a2[2,3])

for row in a2:          #迭代行
    print(row)
    
for row in a2.T:        #迭代列
    print(row)

print(a2.flatten())     #转化为一维   
for item in a2.flat:    #迭代元素
    print(item)