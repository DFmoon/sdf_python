#-*-coding:utf-8-*-
import pandas as pd
import numpy as np

dates=pd.date_range('20180101',periods=6)
df1=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df1.iloc[0,1]=np.nan
df1.iloc[1,2]=np.nan
print(df1)

#丢掉缺失数据
print(df1.dropna(axis=0,how='any'))     #丢掉含有nan的任何一行
print(df1.dropna(axis=0,how='all'))     #丢掉全部为nan的行
print(df1.dropna(axis=1,how='any'))     #丢掉含有nan的任何一列
print(df1.dropna(axis=1,how='all'))     #丢掉全部为nan的列

#填充缺失数据
print(df1.fillna(value=0))              #缺失补0
print(df1.isnull())                     #是否缺失数据，缺失为true
print(np.any(df1.isnull())==True)       #至少有一个数据丢失     
