## Sam Bonning - Assignment 1 - Fizz Buzz file
## test cases should run as follows:
## inputs through sys or user input --> 
##	positive number: runs 
##	negative number: re-requests until positive & runs
##	zero: runs
##	non-number e.g. text: re-requests until positive integer then runs
##	positive float - rounds to int and runs
##	no input - re-requests until positive integer and runs

##TEST LOG: user input passed, sys input passed


import sys
n = "tbd"

if sys.argv[1:2] == []:
	n = input ("How many should we count to in our FizzBuzz game?")

else:
	n = sys.argv[1]
	
while type(n) != int:  
	try:
		n = float(n)
		## this code is to convert to float before int because otherwise python isn't able to recognize a decimal
		n = int(n)
		if n < 1:
			print ("please try a positive integer")
			n = input ("How many should we count to in our FizzBuzz game?") 
	except:
		print ("try again, with a positive integer")
		n = input ("How many should we count to in our FizzBuzz game?") 
# elif sys.argv[1:2] != []:
# 	for a in sys.argv[1:2]:
# 		n = a
# 		try:
# 			n = float(n)
# 			n = int(n)
# 			if n < 1:
# 				print ("please try a positive integer"
# 				n = str(n)
# 				## I can see that this piece of code kicks out to the while loop with a negative integer 
# 				## but the except runs for a string input such as text. Why?
# 		except:
# 			print ("try again, with a positive integer")
# 		while type(n) != int: 
# 			n = input ("How many should we count to in our FizzBuzz game?")  
# 			try:
# 				n = float(n)
# 				## this code is to convert to float before int because otherwise python isn't able to recognize a decimal
# 				n = int(n)
# 				if n < 1:
# 					print ("please try a positive integer")
# 					n = str(n)
# 					## converts n to a string to kick it out of the try loop
# 			except:
# 					print ("try again, with a positive integer")
# else:
# 	print ("You broke my game!")

print ("FizzBuzz counting up to", n)

counter = 1
n = int(n)

while counter <= n:
	if counter % 5 == 0 and counter % 3 == 0:
		print ("FizzBuzz")
	elif counter % 3 == 0:
		print ("Fizz")
	elif counter % 5 == 0:
		print ("Buzz")
	else:
		print (int(counter))
	counter += 1

print ("all done!")