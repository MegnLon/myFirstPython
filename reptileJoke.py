#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com/')

# elem=driver.find_element_by_name("wd")
# elem.send_keys("cxy61")
# elem.send_keys(Keys.RETURN)
# print driver.page_source
dr=webdriver.Chrome()
dr.get('https://www.qiushibaike.com/')
#获取id为content-left的元素
main_content=dr.find_element_by_id('content-left')
#获取class为content的元素
contents=main_content.find_elements_by_class_name('content')

i=1
for content in contents:
	print(str(i)+'.'+ content.text+'\n')
	i+=1
dr.quit()