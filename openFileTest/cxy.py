#!/usr/bin/env python
#coding:utf-8

# fileObj=open("test1.txt","wb")

# print u"文件名称是：",fileObj.name
# print u"文件是否关闭:",fileObj.closed
# print u"文件访问模式:",fileObj.mode
# print u"文件末尾是否强制加空格：",fileObj.softspace
# fileObj.write(" hello ,world.\n");
# fileObj.close()
# fileObj=open("test1.txt","r+")
# str=fileObj.read();
# print u"文件的内容是：",str
# fileObj.close()
# import os
# os.rename("test1.txt","test2.txt")
# os.remove("test2.txt")
import os
from Tkinter import *
#写入日记
def write():
	label.config(text="写日记模式")
	textVar.set("")
	text.delete("0.0","end")	
	listBox.pack_forget()
	entry.pack()
	text.pack()

#创建日记文件夹
def initDiary():
	dir=os.getcwd()
	list=os.listdir(dir)
	haveDiary=False
	for item in list:
		if item=="diary":
			haveDiary=True
	if haveDiary==False:
		os.mkdir("diary")
	os.chdir("./diary")
initDiary()

#保存
def save():
	title=textVar.get()+".txt"
	content=text.get("0.0","end")
	# if title!=".txt":

	# 	dir=os.getcwd()
	# 	list=os.listdir(dir)
	# 	for item  in list:
	# 		if title==item:
	# 			label.config(text="标题重复，重新修改")
	# 		return


	# 	fileObj=open(title,"wb")
	# 	fileObj.write(content)
	# 	fileObj.close()
	# 	label.config(text="已保存")
	# else:
	# 	label.config(text="请输入标题")

	#不使用return时的方法
	# titleIsRepet=False
	# dir=os.getcwd()
	# list=os.listdir(dir)
	# for item in list:
	# 	if title==item:
	# 		titleIsRepet=True
	# if title!=".txt" and titleIsRepet==True:
	# 	label.config(text="标题重复，重新修改")
	# elif title!=".txt" and titleIsRepet==False:
	# 	fileObj=open(title,"wb")
	#  	fileObj.write(content)
	#  	fileObj.close()
	#  	label.config(text="已保存")
	# else:
	#  	label.config(text="请输入标题")

	if title==' ':
		label.config(text="请输入标题")
	else:
		s=socket.socket()
		s.connect(('127.0.0.1',1234))
		print s.recv(1024)
		dict={'title':title,'content':str(content)}
		s.send(str(dict))
		data=s.recv(1024)
		s.close()
		label.config(text=data)






#看日记模式
def read():
	listBox.delete(0,END)

	showText="看日记模式"
	s=socket.socket()
	s.connect(('127.0.0.1',1234))
	print s.recv(1024)
	s.send("read")
	data=s.recv(2048)
	dict=eval(data)
	s.close()

	# dir=os.getcwd()
	# list=os.listdir(dir)
	# showText="看日记模式"
	if len(list)==0:
	 	showText+="（日记本是空的）"
	label.config(text=showText)
	# for item in list:
	# 	listBox.insert(0,item)

	for item in dict.values():
		string =str(item['id'])+ ':'+item['title']
		listBox.insert(0,string)

	listBox.bind('<Double-Button-1>',showDiary)
	entry.pack_forget()
	text.pack_forget()
	listBox.pack()


#显示日记模式
def showDiary(event):
	title=listBox.get(listBox.curselection())
	# showTitle=title[:-4]
	textVar.set(showTitle)

	id=title.split(':')[0]
	data='show'+id

	s=socket.socket()
	s.connect(('127.0.0.1',1234))
	print s.recv(1024)
	s.send(data)
	data=s.recv(1024)
	content=eval(data)['content']
	s.close()

	# fileObj=open(title,"r+")
	# content=fileObj.read()
	text.delete("0.0","end")
	text.insert("end",content)
	# fileObj.close()
	listBox.pack_forget()
	entry.pack()
	text.pack()

root =Tk()
root.geometry('500x400')
root.title("程序媛日记本")

# btn=Button(root,text="这是个按钮")
# btn.pack()

# label=Label(root)
# label.pack()
# label.config(text="这是个演示程序")

saveBtn=Button(root,text="保存",command=save)
saveBtn.pack(side=LEFT,anchor='sw')

quitBtn=Button(root,text="退出",command=quit)
quitBtn.pack(side=RIGHT,anchor='se')

writeBtn=Button(root,text="写日记",command=write)
writeBtn.pack(side=BOTTOM,anchor='s')

readBtn=Button(root,text="看日记",command=read)
readBtn.pack(side=BOTTOM,anchor='s')

textVar=StringVar()
entry=Entry(root,textvariable=textVar)
text=Text(root)
listBox=Listbox(root,height=300)
# listBox.pack()
# list=["apple","orange","milk","water"]
# for item in list:
# 	listBox.insert(0,item)
label=Label(root)
label.pack()


root.mainloop()