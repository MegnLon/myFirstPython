#!/usr/bin/env python
#coding: utf-8
dict1={
	"what's your name"       :"i am xiaofeng",
	"how old are you"        :"i am 21 old"
}
flag='c'
work=True

print u"hi,friends,i am a robot"
while flag=='c' or 't':
	flag=raw_input("input your choose,chatting is 'c',teaching is 't',quit is 'q' : ")
	if flag=='t':
		question=raw_input("input new question :")
		answer=raw_input("input new answer :")
		dict1['question']='answer'
		print "i can  remenber the question"
		continue

	elif flag=='c':
		if len(dict1)==0:
			print u"我还不还回答问题，请教我"
			break
		chat_word=raw_input("input your question:")
		for key in sorted(dict1.keys()):
			if str(chat_word)==key:
				work=True 
				print dict1[chat_word]
				break
			else:
				work=False
		if work==False:
			print u"我还不会回答这个问题"
			work=True 
	elif flag=='q':
		print u"我们下次再会"
		break

