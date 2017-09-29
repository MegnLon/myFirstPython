猜数字的错误
number= int(input('猜猜数字：'))
number=input(unicode('输入整数'，'utf-8').encode('gbk'))
#str=raw_input('raw_input:');
#str=raw_input(unicode('row_input请输入:','utf-8').encode('gbk'));
str=raw_input(u"请输入");
#############
str=raw_input(u"raw_input请输入:");
print u'raw_input的内容是：',str
str2=input('input:');
print str2
报错信息：
raw_input请输入:feng
raw_input的内容是： feng
input:feng
Traceback (most recent call last):
  File "hello.py", line 83, in <module>
    str2=input('input:');
  File "<string>", line 1, in <module>
NameError: name 'feng' is not defined

