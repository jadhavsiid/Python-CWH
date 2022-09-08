# Recursions : Recursive Vs Iterative Approach

#Iterative Approach:
def factorial(n): #Defining a function.
    """ :Parameter n : Input
            :return: n * n-1 * n-2 * n-3......1
    """
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac
inp = int(input("Enter the number whose Factorial you want: "))
print(factorial(inp)) #Declaring a function.

# Recursive Approach
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number whose Factorial you need: "))
print(fact(n))

"""Quiz: Write a function to print a fibonacci series: 0,1,1,2,3,5...."""
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#     print(fibonacci(n))

""" Debate : Recursive vs Iterative Approach
--> Recursive method can be hectic during Debugging.
--> Iterative method can be easily debugged but one has to write more lines of code."""


