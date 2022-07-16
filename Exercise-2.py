"""Exercise-2: Faulty Calculator:
45*3 = 555, 56+9 = 77, 56/6 = 4 """
""" Problem Statement: Design a Calculator which will Correctly Solve all the Problems except the above one.
Your Program should take operator and two numbers as input from user and return the result."""
print("Enter 1st number:")
num1=int(input())
print("Enter 2nd number:")
num2= int(input())
print("Select a Operator: +,-,*,/,%")
op=input()
if num1 == 45 and num2 == 3 and op == "*":
    print("Your Answer is : 555")
elif num1 == 56 and num2 == 9 and op == "+":
    print("Your Answer is : 77")
elif num1 == 56 and num2 == 6 and op == "/":
    print("Your Answer is : 4")
elif op == "+":
    add = int(num1) + int(num2)
    print("Your Answer is: ",add)
elif op == "-":
    minus = int(num1) - int(num2)
    print("Your Answer is: ",minus)
elif op == "*":
    num4 = int(num1) * int(num2)
    print("Your Answer is: ",num4)
elif op == "/":
    dev = int(num1) / int(num2)
    print("Your Answer is: ",dev)
else:
    print("Sorry we don't do that here !")
