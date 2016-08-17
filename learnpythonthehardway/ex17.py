from sys import argv # inputing the value during running the program	
from os.path import exists # defining

script, from_file, to_file = argv # Assigning inputed argv value to 'to_file'

print "Copying from %s to %s" % (from_file, to_file) # printing

in_file = open(from_file) # opening file
indata = in_file.read() # reading file
# we could do these two on one line 
# using target.truncate()

print "The input file is %d bytes long" % len(indata) # printing

print "Does the output file exist? %r" % exists(to_file) # printing along with exists(to_file) function
print "Ready, hit RETURN to continue, CTRL-C to abort." # printingv
raw_input() # inputing

out_file = open(to_file, 'w') # opening file
out_file.write(indata) # writing file

print "Alright, all done." # printing

out_file.close()
in_file.close()
# during run 1) echo "This is a test file." > test.txt
# 2) cat test.txt
# 3) python ex17.py test.txt new_file.txt