coding:utf-8
import dataTest
import socket
import re
#表名
name='diary'
#创建表
dataTest.DB().initTable(name)
#插入数据
dataTest.DB().insertData(name,('title100','content100'))
#删除数据
dataTest.DB().deleteData(name,2)
#修改数据
dataTest.DB().updateData(name,10,('title300','content300'))
#查找数据
dataTest.DB().serachData(name,10)
#打印全部数据
dataTest.DB().showAllData(name)
#关闭链接
dataTest.DB().close()