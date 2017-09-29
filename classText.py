#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
class Qiubait:
	def __init__(self):
		self.dr=webdriver.Chrome()
		self.dr.get('https://www.qiushibaike.com/')

	def print_content(self):
		main_content=self.dr.find_element_by_id('content-left')
		contents=main_content.find_elements_by_class_name('content')

		i=1
		for content in contents:
			print(str(i)+'.'+content.text+'\n')
			i+=1
		self.quit()

	def quit(self):
		self.dr.quit()
Qiubait().print_content()
