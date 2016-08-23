from sys import argv

script, input_file = argv # Assigning the value 

def print_all(f): # defining function
    print f.read() # printing

def rewind(f): # defining function
    f.seek(0)

def print_a_line(line_count, f): # printing
    print line_count, f.readline()

current_file = open(input_file) # opening file

print "First let's print the whole file:\n" # printing and assigning new line

print_all(current_file)

print "Now let's rewind, kind of like a tape." # printing

rewind(current_file)

print "Let's print three lines:" # printing

current_line = 1
print_a_line(current_line, current_file) # printing lines of the file

current_line = current_line + 1
print_a_line(current_line, current_file) # printing lines of the file

current_line = current_line + 1
print_a_line(current_line, current_file) # printing lines of the file 