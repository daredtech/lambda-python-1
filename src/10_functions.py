# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# Read a number from the keyboard
# Print out "Even!" if the number is even. Otherwise print "Odd"

num = input("Enter a number: ")
num = int(num)

# YOUR CODE HERE

def even_or_odd(number):
	if number%2 == 0:
		print("Even!")
	else:
		print('Odd')

even_or_odd(num)