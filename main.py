import sys

def multiply (a, b):
	return a * b

def add(a, b):
	return a + b

if len(sys.argv) == 3:
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])
	print(multiply(num1, num2))
else:
	print("invalid number of arguments")

