#-*-coding:utf-8-*-
import pandas as pd
import numpy as np

#concat和append************************************************************************
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
df4=pd.DataFrame(np.ones((3,4))*3,columns=['b','c','d','e'],index=[1,2,3])
print(df1)
print(df2)
print(df3)
print(df4)

res1=pd.concat([df1,df2,df3],axis=0,ignore_index=True)      #纵向合并，ignore_index=True忽略原始索引号
print(res1)

res2=pd.concat([df3,df4],join='outer',ignore_index=True)    #填补合并
print(res2)
res3=pd.concat([df3,df4],join='inner',ignore_index=True)    #裁剪合并
print(res3)

res4=pd.concat([df3,df4],axis=1,join_axes=[df3.index])      #按照df3的索引进行合并
print(res4)

res5=df1.append(df2,ignore_index=True)                      #追加数据至末尾
print(res5)
res6=df1.append([df2,df3],ignore_index=True)                #追加多项数据至末尾
print(res6)

s1=pd.Series([1,2,3,4],index=['a','b','c','d'])             #追加单行数据
res7=df1.append(s1,ignore_index=True)
print(res7)
print('\n\n')

#merge*****************************************************************************
left=pd.DataFrame({'key':['k0','k1','k2','k3'],
                   'key1':['k0','k0','k1','k2'],
                   'key2':['k0','k1','k0','k1'],
                   'A':['a0','a1','a2','a3'],
                   'B':['b0','b1','b2','b3']})
right=pd.DataFrame({'key':['k0','k1','k2','k3'],
                    'key1':['k0','k1','k1','k2'],
                    'key2':['k0','k0','k0','k0'],
                    'C':['c0','c1','c2','c3'],
                    'D':['d0','d1','d2','d3']})
print(left)
print(right)

res8=pd.merge(left,right,on='key')      #基于key进行合并
print(res8)

res9=pd.merge(left,right,on=['key1','key2'],how='inner')    #只考虑两项中相同的key1、key2截断合并
print(res9)
res10=pd.merge(left,right,on=['key1','key2'],how='outer')   #只考虑两项中相同的key1、key2填补nan合并
print(res10)
res11=pd.merge(left,right,on=['key1','key2'],how='left')    #基于left中的key1、key2合并
print(res11)
res12=pd.merge(left,right,on=['key1','key2'],how='right')   #基于right中的key1、key2合并
print(res12)
res13=pd.merge(left,right,on=['key1','key2'],how='right',indicator=True)    #indicator指示合并详细信息
print(res13)
res14=pd.merge(left,right,on=['key1','key2'],how='right',indicator='sdf')   #indicator列重命名
print(res14)
print('\n\n')

#index*****************************************************************************
df_left=pd.DataFrame({'A':['a0','a1','a2'],'B':['b0','b1','b2']},index=['k0','k1','k2'])
df_right=pd.DataFrame({'C':['c0','c1','c2'],'D':['d0','d1','d2']},index=['k0','k2','k3'])
print(df_left)
print(df_right)

res15=pd.merge(df_left,df_right,left_index=True,right_index=True,how='outer')
print(res15)

#overlapping***********************************************************************
boys=pd.DataFrame({'k':['k0','k1','k2'],'age':[26,34,27]})
girls=pd.DataFrame({'k':['k0','k0','k3'],'age':[25,30,29]})
res16=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res16)