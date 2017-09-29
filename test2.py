#!/usr/bin/env python
#coding: utf-8

import re
pattern=re.compile('hello')
match=pattern.match('hello cxy61!')
print "match:",match
if match:
	print "match.group():",match.group()
else:
 	print"no match"

print u"以上是有匹配结果的事例"
print u"*********************"
print u"以下是无匹配结果的事例"

pattern2=re.compile(r'Python')
match2=pattern2.match('hello cxy61')

print match2
if match2:
 	print match2.group()
else:
 	print "no match"

print "************************"
print "*********Search()******************"

pattern3=re.compile('hello')
match3=pattern3.search('hello cxy61!')

print "match3:",match3
if match3:
	print match3.group()
else:
	print "no match"

print "******search()，match()**************"
string="i like Python"
pattern4=re.compile('Python')

match4=pattern4.match(string)
search4=pattern4.search(string)

if match4:
	print u"match()的结果是:"+match4.group()
else:
	print u"match()的结果是:No match"
if search4:
	print u"search()的结果是:"+search4.group()
else:
	print u"search()的结果是:No search"

print "********sub()**********"
time="2017-9-26"
pattern5=re.compile(r'\D')
sub=pattern5.sub("/",time)
print "sub:",sub
print re.sub(r'\D','/',time)
# while True:
# 	phone=raw_input('phone number:')
# 	pattern6=re.compile('^0\d{2,3}\d{7,8}$|1[3578]\d{9}$|147\d{8}$')
# 	match6=pattern6.match(phone)
# 	if match6:
# 		print(match6.group())
# 	else:
# 		print("error")

import sqlite3
connect =sqlite3.connect("sqltest.db")
connect.close()