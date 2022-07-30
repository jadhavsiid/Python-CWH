# Anonymous/Lambda Functions in Python
def add(a,b): #Defining a Normal Function
    return a+b
plus = lambda x,y: x+y #Defining a lambda Function.
print(add(4,6)) #Declaring a Normal Function
print(plus(4,6)) #Declaring a Lambda Function.

def a1(a):
    return a[1]
a = [[1,14],[5,6],[8,23]]
a.sort(key=a1)
print(a)
a.sort(key=lambda x:x[1])
print(a)
