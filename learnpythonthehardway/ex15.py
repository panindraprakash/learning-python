from sys import argv # defining

script, filename = argv # inputing the value during running the program		

txt = open(filename) # using 'open' function key we are opening the inputed filename

print "Here's your file %r:" % filename # printing along with the value of filename
print txt.read() # using 'text.read' function we are printing the content in the given file

print "Type the filename again:" # printing
file_again = raw_input("> ") # inputing the value

txt_again = open(file_again) # Assigning the vales to text_again

print txt_again.read() # '.read' function we are printing the content in the defined file