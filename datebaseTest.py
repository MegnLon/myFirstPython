#!usr/bin/env python
#coding: utf-8
import sqlite3
connect=sqlite3.connect("test.db")
cursor=connect.cursor()

cursor.execute("CREATE TABLE  diary (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,content TEXT)") 

print u"*****增*******\n"
cursor.execute("INSERT INTO diary VALUES (NULL,'title1','content1')")
cursor.execute("INSERT INTO diary(title,content) VALUES ('title2','content2')")
for row in cursor.execute("SELECT * FROM diary"):
	print row


print u"*******删********"
cursor.execute("DELETE FROM diary WHERE id =1")
for row in cursor.execute("SELECT *FROM diary"):
	print row

print u"*****改*****"
cursor.execute("UPDATE diary SET title='title0',content='content0' WHERE id=2")
for row in cursor.execute("SELECT *FROM diary"):
	print row

items=[("title0","content0"),("title1","content1"),("title2","content2")]
cursor.executemany("INSERT INTO diary(title,content) VALUES (?,?)",items)
print u"插入多条数据后的表:"
for row in cursor.execute("SELECT *FROM diary"):
	print row

print u"查id 为5 的数据："
cursor.execute("SELECT *FROM diary WHERE id=5")
print cursor.fetchall()

print u"查 title为title0 的数据："
cursor.execute("SELECT *FROM diary WHERE title='title0'")
print cursor.fetchall()

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# for item in cursor.fetchall():
# 	print item

cursor.close()
connect.close()




