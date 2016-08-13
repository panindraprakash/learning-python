formatter = "%r %r %r %r" # assigning the valure %r %r %r %r to formatter

print formatter % (1, 2, 3, 4) # assigning the vale of 1,2,3,4 to formatter %r respectively and printing it in one line.
print formatter % ("one", "two", "three", "four") # assigning the value of one,two,three,four to formatter %r respectively and printing it in one line
print formatter % (True, False, False, True) # assigning the vale of True, False, False, True to formatter %r respectively and printing it in one line.
print formatter % (formatter, formatter, formatter, formatter) # assigning the value of formatter,formatter,formatter,formatter to formatter %r respectively and printing it in one line.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) # assigning value to formatter %r and printing even though lines are writen in diffrent line since we are using comma it will print in same line
