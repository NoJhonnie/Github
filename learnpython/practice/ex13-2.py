from sys import argv

script, name, sex, age = argv

argv1 = raw_input("What is your name?")
argv2 = raw_input("What is your gender?")
argv3 = raw_input("How old are you?")

print "The script is called:", script 
print "Your name is %s: %s" %(name, argv1)
print "Sex is %s:%s" %(sex,argv2)
print "How old are you? %s:%s" %(age,argv3)