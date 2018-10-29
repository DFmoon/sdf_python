#-*-coding:utf-8-*-
import numpy as np

#合并**************************************************************************
A=np.array([[1,1,1],[1,1,1]])
B=np.array([[2,2,2],[2,2,2]])

C=np.vstack((A,B))      #上下合并
print(C)

D=np.hstack((A,B))      #左右合并
print(D)

E=np.concatenate((A,B,B,A),axis=0)        #自定义行合并与列合并
print(E)
print('\n\n')

#分割**************************************************************************
a1=np.arange(12).reshape((3,4))
print(a1)

print(np.split(a1,2,axis=1))        #横向均等分割，即对列分割，分成2块
print(np.split(a1,2,axis=1)[0])
print(np.split(a1,2,axis=1)[1])

print(np.split(a1,3,axis=0))        #纵向均等分割，即对行分割，分成3块
print(np.split(a1,3,axis=0)[0])
print(np.split(a1,3,axis=0)[1])
print(np.split(a1,3,axis=0)[2])

print(np.array_split(a1,2,axis=0))  #纵向不等分割，分成2块
print(np.array_split(a1,2,axis=0)[0])
print(np.array_split(a1,2,axis=0)[1])

print(np.vsplit(a1,3))
print(np.hsplit(a1,2))
print('\n\n')

#复制**************************************************************************
a2=np.arange(12).reshape((3,4))
print(a2)

b=a2            #浅复制，相互关联
b[2,3]=56
print(a2)

c=a2.copy()     #深复制，只复制值，没有关联,numpy中的深复制，和copy中的copy和deepcopy不同
c[2,3]=30
print(a2)
print(c)

