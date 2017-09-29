#!/usr/bin/env python
#coding:utf-8
while 1:
	try:
		num1=raw_input("input dividend:")
		num2=raw_input("input divisor:")
		result=int(num1)/int(num2)
	#except ZeroDivisionError:
	#	print u" 0 不能做除数"+'\n'
	#except ValueError:
	#	print u"请输入空值或字母"+'\n'
	except BaseException:
		print u"出现异常"+'\n'

	else:
		print u'运算结果为：%d' % result+'\n'