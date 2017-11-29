from sys import argv

script, user_name = argv
prompt = '>>>>'

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "Where do you like %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Can we make a friend?"
friends = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. 
You also said %r about make friends with me.Nice.""" %(likes, lives, computer, friends)