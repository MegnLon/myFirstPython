#coding:utf-8
import sqlite3
class DB:
	def __init__(self):
		self.connect=sqlite3.connect("test.db")
		self.cursor=self.connect.cursor
	def searchTable(self,tableName):
		flag=False
		self.cursor.execute("SELECT name FROM sqlite_master WHERE type=''")