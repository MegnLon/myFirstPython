#!/usr/bin/env python
#coding: utf-8 

for letter in 'apple':
	print u"apple 中的字母有：",letter
animals=['cat','dog','monkey']
for animal in animals:
	print u"动物有:",animal
for index in range(len(animals)):
	print u'动物有index:',animals[index]
print"*****************"
str1="hello"
str2="world"
print u'str1+str2的结果是：',str1+str2
print str1*2
name="feng"
age=21
print"the girl's name is %s,age is %d" %(name,age)
list1=['cat','mouse','dog',300,200]
print 'list1[0]:',list1[0]
print 'list1[1:3]',list1[1:3]
list1[3]='fox'
print u'第一次跟新:',list1
list1.append(100)
print u'第二次跟新:',list1
del list1[1]
print u'第三次跟新：',list1
print len([1,2,3])
print [1,2,3]+[1,2,3]
tup1=(3,4,5,6,7)
tup2=('cat','dog',100,200)
tup3='x','y','z'
print "tup1[0]:",tup1[0]
print "tup2[1:3]:",tup2[1:3]
print "tup3:",tup3
#tup1[0]=9
#print "tup1第一次修改",tup1
tup1=tup1+tup2
print "tup1",tup1
del tup1
#print tup1
print "tup2的长度:",len(tup2)
tup1=(100,)*4
print "tup1:",tup1
for x in (1,2,3):
	print "x的值：",x

dict={'name':'apple','color':'red'}
print u"字典dict['name']:",dict['name']
dict['color']='green'
print dict
dict['location']='cumt'
print dict
del dict['location']
print dict
dict.clear()
print dict
del dict
print dict
dict1={'name':'apple','color':'red'}
print dict1.keys()

import time
print time.time()
print time.localtime(time.time())
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

import calendar
print calendar.month(2017,9)
import time
print u"今天的日期是:",time.strftime('%A',time.localtime())

def my_print(str):
	print str;
	return;
my_print('this is ele class')
my_print('nice,this is craze')

#str=raw_input('raw_input:');
#str=raw_input(unicode('row_input请输入:','utf-8').encode('gbk'));
#str=raw_input(u"raw_input请输入:");
#print u'raw_input的内容是：',str
#str2=input('input:');
#print str2


