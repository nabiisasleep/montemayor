# 1. Get input for two numbers.
# 2. Calculate the sum of the two numbers.
# 3. Calculate the product of the two numbers.
# 4. Calculate the square of each number.
# 5. Calculate the cubic of each number.
# 6. Calculate the exponential of each number.
# 7. Display the calculated results.

def get_input():
# Function to get input for two numbers
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    operation = input("enter the operation(+, -, *, /, sq, cb, exp):")
    	if operation in['sq','cb','exp']:
    		return num1, operation
    	return num1, num2 operation

# Function to perform the selected operation
def perform_operation (num1, num2, operation):
	if operation== "+":
	return calculate_sum(num1, num2)

elif operation =="-":
	return num1 - num2

elif operation =="*":
	return calculate_product(num1, num2)

elif operation =="/":
	return num1 / num2

elif operation =="sq":
	return calculate_square(num1)

elif operation =="cb":
	return calculate_cubic(num1)

elif operation =="exp":
	power= float(input("Enter the power: "))
	return calculate_exponential(num1, power)

else:
	print("invalid operation")
	return None

def calculate_sum(num1, num2):
# Function to calculate the sum of two numbers
    return num1+ num2

def calculate_product(num1, num2):
# Function to calculate the product of two numbers
    return num1*num2

def calculate_square(num):
# Function to calculate the square of a number
    return num**2

def calculate_cubic(num):
# Function to calculate the cubic of a number
    return num**3

def calculate_exponential(num):
# Function to calculate the exponential of a number
    return num**power

    # Call main Function
if __name__=="__main__":
    main()