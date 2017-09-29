coding:utf-8
import sqlite3
class DB:
	def __init__(self):
		self.connect=sqlite3.connect("test.db")
		self.cursor=self.connect.cursor()

	def searchTable(self,tableName):
		flag=False
		self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
		for item in self.cursor.fetchall():
			if item[0]==tableName:
				flag=True
				break
		return flag

	def initTable(self,tableName):
		if self.searchTable(tableName)==False:
			sql="CREATE TABLE "+ tableName +" (id INTEGER　PRIMAY　KEY AUTOINCREMENT,title TEXT，content TEXT)"
			print u"创建表成功"
		else:
			print u"该表已存在"

	def insertData(self,table,data):
		sql="INSERT INTO "+tableName+"(title,content) VALUES (?,?)"
		self.cursor.execute(sql,data)
		self.connect.commit()
		return "保存成功"

	def deleteData(self,tableName,id):
		sql="DELETE FROM　"+ tableName +"WHERE id ="+ str(id)
		self.cursor.execute(sql)
		self.connect.commit()
		return "删除成功"

	def updataData(self,tableName,id,data):
		sql="UPDATE　"+tableName+" SET title='"+ data[0] +"',content='"+ data[1]+"' WHERE id="+ str(id)
		self.cursor.execute(sql)
		self.connect.commit()
		return "修改成功"

		def searchData(self,tableName,id):
			sql="SELECT *FROM "+tableName+"WHERE id ="+ str(id)
			self.cursor.execute(sql)
			tup=self.cursor.fechone()
			dict={'title':tup[1],'content':tup[2]}
			return str(dict)

		def showAllData(self,tableName):
			sql="SELECT *FROM "+tableName
			for row in self.cursor.execute(sql):
				print row

		def getDataDict(self,tableName):
			dict ={}
			i=0
			sql="SELECT *FROM "+tableName
			for row in self.cursor.execute(sql):
				item={'id':row[0],'tile':row[1]}
				dict[str(i)]=item
				i+=1
			return str(dict)

		def close(self):
			self.cursor.close()
			self.connect.close()