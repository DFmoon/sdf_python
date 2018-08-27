#-*-coding:utf-8-*-
import pandas as pd
import numpy as np

dates=pd.date_range('20180101',periods=6)
df1=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

#筛选***********************************************************************************
print(df1)
print(df1['A'])                     #选择列
print(df1.A)
print(df1[0:3])                     #选择行
print(df1['20180101':'20180103'])

print(df1.loc['20180102'])          #标签筛选行
print(df1.loc['20180102',['A','B']])#标签联合筛选行列

print(df1.iloc[3,2])                #数字筛选特定元素
print(df1.iloc[0:3,1:3])            #数字筛选特定行列
print(df1.iloc[[1,2,4],1:3])        #数字筛选特定行列

print(df1.ix[0:3,['A','D']])        #数字和标签混合筛选

print(df1[df1.A>8])                 #条件筛选

#赋值***********************************************************************************
df1.iloc[2,1]=111
df1.loc['20180102','A']=222
df1.A[df1.A==0]=333
df1.B[df1.A>4]=0
df1['F']=np.nan     #添加列
df1['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6))#此时的index必须和原数据一致
print(df1)