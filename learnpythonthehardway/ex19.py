def cheese_and_crackers(cheese_count, boxes_of_crackers): # defining
    print "You have %d cheeses!" % cheese_count # printing along with the value of cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers # printing along with the value of boxes_of_crackers
    print "Man that's enough for a party!" # printing
    print "Get a blanket.\n" # printing ans assigning new line.


print "We can just give the function numbers directly:" # printing
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:" # printing
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:" # printing
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:" # printing
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
