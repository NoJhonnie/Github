#coding=utf-8
from sys import exit
from random import randint

def death():
    quips = ["You died. Youkinda suck at this.",
            "Nice job, you died ...jackass.",
            "Such a luser.",
            "I have a small puppy that's better at this."]
    print quips(randint(0, len(quips)-1))   #在quips随机选出一个死亡表述
    exit(1)
    
def central_corridor():
    print "The Gothons of planet Percal #25 have incaded your ship and destroyed"
    print "your entire crew. You are the last surviving member and your last"
    print "missing is to get the neutron destruct bomb from the Weapons Armory,"
    print "put it in the bridge, and blow the ship up after getting into an"
    print "escape pod."
    print "\n"
    print "You're running down the central corridor to the Weapons Armory when"
    print "a Gothon	jumps out, red scaly skin, dark grimy teeth, and evil clown co stume"
    print "flowing around his hate filled body. He's blocking the door to the"
    print "Armory and about to pull a weapon to blast you."
    
    action = raw_input(">")
    
    if action == "shoot":
        print """Quick on the draw you yank out your blaster and fire it at the Goth on.
                His clown costume is flowing and moving around his body, which throws off
                your aim. Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother bought him, which
                makes him fly into an insane rage and blast you repeatedly in the face until
                you are dead. Then he eats you."""
        return 'death'
    elif action == "dodge":
        print """Like a world class boxer you dodge, weave, slip and slide right
                as the Gothon's blaster cranks a laser past your head.
                In the middle of your artful dodge your foot slips and you
                bang your head on the metal wall and pass out. You wake up shorly
                after only to die as the Gothon stomps on your head and eats you."""
        return 'death'
    elif action == "tell a joke":
        print """Lucky for you they made you learn Gothon insults in the academy.
                You tell the one Gothon joke you know:ddddfaos foasfoasf oahsf a.
                The Gothon stops, tries not to laugh, the busts out laughing and can't move.
                While he's laughing you run up and shoot him square in the head putting
                him down, then jump through the Weapons Armory door."""
        return 'laser_weapon_armory'
    else:
        print "DOES NOT COMPUTE!"
        return 'central_corridor'
        
def laser_weapon_armory():
    print "many words"
    print "get the bomb. The code is 3 digits."
    code = "%d%d%d" %(randint(1,2),randint(4,5),randint(8,9))
    guess = raw_input("[keypad]>")
    guesses = 0
    
    while guess != code and guesses < 10:
        print "DDDEGN"
        guesses += 1
        guess = raw_input("[keypad]>")
        
    if guess == code:
        print "too many words!"
        return 'the_bridge'
    else:
        print "a little words."
        return 'death'
        
def the_bridge():
    print "words"
    action = raw_input(">")
    
    if action == "throw the bomb":
        print "a few words"
        return 'death'
    elif action == "slowly place the bomb":
        print "..."
        return 'escape_pod'
    else:
        print "Does not compute!"
        return 'the_bridge'
        
def escape_pod():
    print "..."
    good_pod = randint(1,5)
    guess = raw_input("[pod #]>")
    
    if int(guess) != good_pod:
        print "into jam jelly."
        return 'death'
    else:
        print "time. You won!"
        exit(0)
        
ROOMS = {
        'death':death,
        'central_corridor':central_corridor,
        'laser_weapon_armory':laser_weapon_armory,
        'the_bridge':the_bridge,
        'escape_pod':escape_pod
        }
        
def runner(map, start):
    next = start
    
    while True:
        room = map[next]
        print "\n----------------"
        next = room()
        
runner(ROOMS, 'central_corridor')