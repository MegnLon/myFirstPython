#!/usr/bin/env python
#coding:utf-8
import sqlite3
connect=sqlite3.connect("test.db")
cursor=connect.cursor()

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# for item in cursor.fetchall():
# 	print item
def searchTable(str):
	global cursor
	flag=False
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
	for item in cursor.fetchall():
		if item[0]==str:
			flag=True
			break
	return flag

def initTable(str):
	global cursor
	if searchTable(str)==False:
		sql="CREATE TABLE"+str+"(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,content TEXT)"
		cursor.execute(sql)
	else:
		print u"该表已存在"

#插入数据
def insertDate(name,tup):
	global cursor
	global connect
	sql="INSERT INTO "+name+"(title,content) VALUES (?,?)"
	cursor.execute(sql,tup)
	connect.commit()

#删除某条数据（表名，主键）
def deleteDate(name,id):
	global cursor
	global connect
	sql="DELETE FROM "+name+" WHERE id ="+str(id)
	cursor.execute(sql)
	connect.commit()

#根据id修改数据，(表名，主键，tup)
def updateDate(name,id,tup):
	global connect
	global cursor
	sql="UPDATE "+ name +" SET title='"+ tup[0] +"', content='"+ tup[1] +"' WHERE id="+str(id)
	cursor.execute(sql)
	connect.commit()

#根据id查找数据（表名，id）
def searchId(name,id):
	global cursor
	sql="SELECT *FROM"+name+"WHERE id="+str(id)
	cursor.execute(sql)
	print u"查找的数据为：",cursor.fetchone()

#根据title查找数据（表名，title）
def searchTitle(name,title):
	global cursor
	sql="SELECT *FROM "+ name +" WHERE title= "+ str(title)
	cursor.execute(sql)
	print u"查找的数据为：",cursor.fetchone()

initTable('diary')
insertDate("diary",('title99','cotent99'))
deleteDate("diary",5)
updateDate("diary",18,('title100','content100'))
searchTitle("diary",10)
for row in cursor.execute("SELECT *FROM diary"):
	print row


cursor.close()
connect.close()