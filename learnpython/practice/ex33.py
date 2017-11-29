#encoding=utf-8
#定义一个函数，参数maxnums定义添加的最大值，num定义每次增加的值
def plus_numbers(maxnums, num):
	i = 0
	numbers = []
	'''
	while i < maxnums:
		print "At the top i is %d" % i
		numbers.append(i)
		i += num
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	'''
	for i in range(0,10):
		print "At the top i is %d" %i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The Numbers:"
	for nums in numbers:
		print nums
		
plus_numbers(10, 2)