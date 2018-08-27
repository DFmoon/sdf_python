#-*-coding:utf-8-*-
import copy
import pickle

#print
print('#print')
print('21678y')
print('\'')
print('phs'+'789')
print('ewr'+str(2))
print(3+1)
print(1.2+8)
print(int(1.2)+8)

#基础运算
print('#基础运算')
print(2*3)
print(2**3)     #平方
print(9/4)
print(9//4)     #取整
print(9%4)
a,b,c=1,2,3
print(a,b,c)

#函数
print('#函数')
def runnian(x):
    if(x%4==0 and (x%100!=0 or x%400==0) ):
        print(x,'是闰年')
    else:
        print(x,'不是闰年')
runnian(2021)

#全局变量
print('#全局变量')
a=20
def fun():
    global a
    a=40
    return a+100
print(a)
print(fun())
print(a)

#读写文件
print('#读写文件')
text='gababdjb\nhasjhdjka\nhidhs'
create_file=open('untitled.txt','w')        #创建一个文件，w为写模式，r为只读模式,a为追加模式
create_file.write(text)
create_file.close()
appended_file=open('untitled.txt','a')        #追加文件内容
appended_file.write('\n891638168')
appended_file.close()
read_file=open('untitled.txt','r')      #读取文件内容,readling是逐行读取
content=read_file.read()
print(content)

#class
print('#class')
class Cal:
    name='df'
    price=78
    def __init__(self,hight,width=13):      #初始化
        self.h=hight
        self.w=width
    def add(self,x,y):      #self是类中默认的代指自身的参数，用于类内调用
        result=x+y
        print(result)
        print(self.name)    #通过self调用自身的属性
    def minus(self,x,y):
        print(x-y)
cal=Cal(32)      #因为有init初始化，必须在创建实例时输入对应的参数，输入的属性值会覆盖已经定义的属性值
print(cal.price)
cal.add(12,34)

#输入
print('#输入')
aa=input('请输入一个数：')     #注意，inpu的返回值是一个字符串
print(aa)

#元组tuple/列表list/字典dictiona
print('#元组tuple/列表list/字典dictiona')
a_tuple=(23,65,3,25,96)
b_tuple=23,65,3,25,96
a_list=[23,65,3,25,96]
print('a_tuple的长度是：',len(a_tuple))
print('a_list的长度是：',len(a_list))
for item in a_tuple:
    print(item)
for index in range(len(a_list)):
    print(index,'=',a_list[index])

a_list.append(3)        #列表相关功能
a_list.insert(1,0)
a_list.remove(96)       #删除的是值
print(a_list)
print(a_list[-2])       #倒数
print(a_list[2:5])      #输出2,3,4位
print(a_list.index(65)) #返回索引
print(a_list.count(65)) #返回出现65的次数
a_list.sort()           #排序，从小到大
print(a_list)
a_list.sort(reverse=True)           #从大到小
print(a_list)

a_dic={'a':23,'b':34,'c':'saa',3:34}
print(a_dic['a'],a_dic['c'],a_dic[3])
del a_dic['a']      #删除
a_dic['d']=7        #增加
print(a_dic)

#zip/lambda/map
print('#zip/lambda/map')        #zip用于合并
a=[2,7,9]
b=[3,0,5]
print(list(zip(a,b,b)))
for i,j in zip(a,b):
    print(i+j)

func=lambda x,y:x*y             #lambda用于定义简单方程
print(func(3,6))

print(list(map(func,[1,8,0],[2,6,4])))  #结合zip和lambda

#深复制和浅复制
print('#深复制和浅复制')
c=[3,0,7]           #浅复制，索引一致，关联变动
d=c
d[0]=22
print(c,d)

e=copy.copy(c)      #浅复制，关联变动深度维，浅度维不关联（数值复制）
e[0]=12
print(c,e)

f=copy.deepcopy(c)  #深复制，仅复制数值
f[0]=34
print(c,f)

#pickle保存提取数据
print('#pickle保存提取数据')
file=open('untitled.pickle','wb')       #wb表示写入二进制的形式
pickle.dump(a_dic,file)                 #装载内容
file.close()

file=open('untitled.pickle','rb')       #rb表示读数据的形式
a_dic1=pickle.load(file)
file.close()
print(a_dic1)

with open('untitled.pickle','rb') as file:      #使用with语句完成后文件会自动关闭，不用手动添加close()
    a_dic2=pickle.load(file)
    print(a_dic2)  
    
#set找不同，set就是一个类
print('#set找不同')
li=['a','d','t','r','a','g','a']
print(li)
li_set=set(li)
print(li_set)

sentence='welcome to my house'  #看成list,大小写敏感
print(sentence)
print(set(sentence))
print()

li_set.add('a')     #set之后只能添加没有重复的元素
li_set.add('k')
print(li_set)

print(li_set.remove('r'))       #移除元素，返回值是none，移除不存在的元素会报错，为避免报错可以用discard代替remove
print(li_set)

set1=copy.deepcopy(li_set)      #set对象的difference和intersection
set2=['d','f','g']
print(set1.difference(set2))    #set1有，set2没有的元素
print(set1.intersection(set2))  #两者都有的元素

li_set.clear()