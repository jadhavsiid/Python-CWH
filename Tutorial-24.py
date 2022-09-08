# Try Except Exception Handling in Python
print("Enter num 1:")
num1 = input()
print("Enter num 2:")
num2 = input()
try:
    print("The sum of num 1 and num2 is:",int(num1)+int(num2))
except Exception as e:
    print(e)
print("This line is very imp") #inorder to print this line irrespective of any errors compiler might face in lines
# before line 10 we use 'Try except Exception handling.'


