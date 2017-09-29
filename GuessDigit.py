#!/usr/bin/env python
#coding:utf-8

#导入随机数
#得到一个随机数
#设置一个输入框，把得到的值
import random 
answer=int (random.uniform(1,10)) 
number=input("guess the number:\n") 

if number==answer:
	print ("you are great!\n")
while number!=answer:
	if number>answer:
		number=int(input("once again\n"))
	if number<answer:
		print u"猜小了"
		number=int(input("once again\n"))
	if number==answer:
		print "right!"
		break
