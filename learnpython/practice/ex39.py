ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')

more_stuff = ["Me", "You", "He", "Corn", "Cat", "Dog", "Boy", "Girl",
            "Banana", "Numbers"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go:", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #print the last one
print stuff.pop()
print " ".join(stuff) #same join(' ', stuff)
print '#'.join(stuff[3:5])  #insert # between stuff[3] and stuff[4]