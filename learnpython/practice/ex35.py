#encoding = utf-8

from sys import exit

def gold_room():
	#定义一个金币屋，判断你拿了多少金币
	print "This room is full of gold!!! How much do you take?"
	how_much = raw_input("Please input the number:")
	
	if how_much.isdigit():
		how_much = int(how_much)
		if how_much < 500:
			print "Nice! You\'re not greedy, you win!"
			exit(0)
		else:
			print "You greedy bastard!"
	else:
		print "Man, learn to type a number. Please input the number:"
		
def bear_room():
	#定义左边是熊的房间，引开挡在门口的熊，穿过门
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	print """[1]take honey	[2]taunt bear	[3]open door"""
	bear_move = False
	
	while True:
		next = raw_input("Please input the number>")
		#判断你采取什么措施，发生相应的事件
		if next == "take honey" or next == "1" or next == "[1]take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" or next == "2" or next == "[2]taunt bear" and not bear_move:
			print "The bear has moved from the door. You can go through it now."
			bear_move = True
		elif next == "taunt bear" or next == "2" or next == "[2]taunt bear" and bear_move:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" or next == "3" and bear_move:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	#定义右边是克苏鲁房间,你是偷跑还是被吃掉头
	print "Here you see the great evil Cthulhu."
	print "He,it,whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("Please input your choose!>")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	#定义死亡原因
	print why, "Good job!"
	exit(0)
	
def start():
	#开始游戏，选择左边或是右边的房间
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	print "(1)right  (2)left"
	
	next = raw_input("Please input your choose!>")
	
	if next == "left" or next == "1":
		bear_room()
	elif next == "right" or next == "2":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()