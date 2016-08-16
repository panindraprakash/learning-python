from sys import argv

script, filename = argv # inputing the value during running the program		

print "We're going to erase %r." % filename # printing along with the value of filename
print "If you don't want that, hit CTRL-C (^C)." # printing
print "If you do want that, hit RETURN." # printing 

raw_input("?") # checking which value is inputed.

print "Opening the file..." # printing
target = open(filename, 'w') # opening the file

print "Truncating the file.  Goodbye!" # printing
target.truncate() # using function

print "Now I'm going to ask you for three lines." # printing

line1 = raw_input("line 1: ") # inputing and assigning to line1
line2 = raw_input("line 2: ") # inputing and assigning to line2
line3 = raw_input("line 3: ") # inputing and assigning to line3

print "I'm going to write these to the file." # printing

target.write(line1) # writing the data of value line1 in the target using 'target.write' function key.
target.write("\n") # creating new line 
target.write(line2) # writing the data of value line1 in the target using 'target.write' function key.
target.write("\n") # creating new line 
target.write(line3) # writing the data of value line1 in the target using 'target.write' function key.
target.write("\n") # creating new line 

print "And finally, we close it." # printing
target.close() # closing the target