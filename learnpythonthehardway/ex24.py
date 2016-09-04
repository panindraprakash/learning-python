print "Let's practice everything."# printing 
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.' # printing

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. 
"""# creating a value to the poem

print "--------------"
print poem # calling poem
print "--------------"


five = 10 - 2 + 3 - 6 # calculating
print "This should be five: %s" % five

def secret_formula(started):  # creating function
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point # printing
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) # printing using values in function secret_formula

start_point = start_point / 10 # calculating

print "We can also do that this way:"# printing
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # printing