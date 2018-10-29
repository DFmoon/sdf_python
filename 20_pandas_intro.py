#-*-coding:utf-8-*-
import pandas as pd
import numpy as np

s=pd.Series([1,3,6,np.nan,44,1])
print(s)

df1=pd.DataFrame(np.arange(12).reshape((3,4)))      #自动生成行列的名称序列
print(df1)

dates=pd.date_range('20180101',periods=6)
print(dates)
df2=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])    #自定义行列的名称序列
print(df2)

df3=pd.DataFrame({'A' : 1.,
                  'B' : pd.Timestamp('20130102'),
                  'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D' : np.array([3] * 4,dtype='int32'),
                  'E' : pd.Categorical(["test","train","test","train"]),
                  'F' : 'foo'})                     #自定义行列的名称序列
print(df3)
#两种方式定义DataFrame,一种是直接引用numpy数据，一种是字典形式，一列一列定义
print(df3.dtypes)
print(df3.index)        #行名
print(df3.columns)      #列名
print(df3.values)       #值
print(df3.describe())       #描述特征（数据量、方差、平均值、、、）
print(df3.T)                #转置
print(df3.sort_index(axis=1,ascending=False))   #横向索引排序，ascending=False表示反向
print(df3.sort_index(axis=0,ascending=False))   #纵向索引排序，ascending=False表示反向
print(df3.sort_values(by='E'))                  #根据元素排序，by='E'指定依据的列

#numpy是序列化的矩阵，pandas为字典形式的numpy，又有行列名
#numpy：np.array()
#pandas:pd.Series()、pd.DataFrame()