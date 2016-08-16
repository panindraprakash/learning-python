from sys import argv # defining 

script, user_name = argv # defining
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script) # printing value of user_name which is given during run time and printing the value of existing script 
print "I'd like to ask you a few questions." # printing
print "Do you like me %s?" % user_name # printing along with the value of user_name 
likes = raw_input(prompt) # Assigning the value of input to likes

print "Where do you live %s?" % user_name # printing along with the value of user_name
lives = raw_input(prompt) # Assigning the value of input to lives

print "What kind of computer do you have?"# printing
computer = raw_input(prompt) # Assigning the value of input to lives

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer) # printing along with the value of likes,lives,computer
