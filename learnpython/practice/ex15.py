#coding = utf-8
from sys import argv #从sys的modules中导入的argv

script, filename = argv #将参数解包传递

txt = open(filename)	#打开filename文件

print "Here's your file %r:" % filename	#打印文件名
print txt.read()	#打印文件内容

print "Type the filename again:"
file_again = raw_input(">>>")	#输入信息
txt_again = open(file_again)	#打开file_again文件
print txt_again.read()	#打印文件内容