# Functions and Docstrings in Python
a=4
b=4
c = sum((a,b)) #Built-in Functions
print(c,'\n')

def function1(): #Defining a function
    print("Hello you are in function1 \n")
print(function1()) #This will print 'None' as it has no retun Statement
(function1()) #Declaring a function

def function2(a,b):
    print("The Sum of two numbers are: ",a+b,'\n')
(function2(5,7))

def function3(a,b):
    """ This is a function which will calculate average of two numbers.""" #Docstring
    avg = (a+b)/2
    print("The avg of two number is:", avg)
    return avg #Return statement is always optional but it is reccomended to use it.
v=(function3(7,8)) #this will give refernce of function3
print(v) #this will print the average

print(function3.__doc__) #This will print docstring of a function.
"""Note: Docstrings are printed to get an description of a function if you're working with a program built by 
different programmer apart from you."""
