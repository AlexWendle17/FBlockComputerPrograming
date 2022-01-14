def add1(n):
	return n+1

def jan5A():
	print("12345")

# output:
#1
#2
#3
#4
#5
def jan5B():
	for a in range(1, 6):
		print(a)

# Ask for a number,
# and then print out all numbers (each on a new 
# libe) from one to the number we typed in
def jan6A():
	number = int(input("type something:"))
	for a in range (1, number + 1000):
		print(a)

jan6A()