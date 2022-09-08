# Variables, Datatypes and Typecasting
# var1 = "Hello World, " #String variable
# var2 = 4 #Integer variable
# var3 = 36.7 #Floating point variable
# var4 = "Siddhesh"
# var5= "26 "
# var6= "30"
# print(type(var1)) #Type function used to identify type of any variable
# print(type(var2))
# print(type(var3))
# print(var2+var3)
# print(var1+var4)
# print(var5+var6)
# print(var5 + var4)
# Typecasting: used to add two number strings instead of concatenating them
# print(int(var5) + int(var6))
# print(10*int(var5) + int(var6))
# print(10* str(int(var5) + int(var6)))
# print(10*"Hello Wolrd\n")
# how to take input from user
print("Enter your number")
inpnum = input() # Storing input as a String
print("You entered:", inpnum)
print("after adding 10:", int(inpnum)+10,'\n')  #Converted input as a string into integer via typecasting.

#Quiz: WAP in Python to add two numbers by taking input from user
print("Enter first number: ")
n1 = input()
print("Enter second number: ")
n2 = input()
print("The addition of two entered number is: ",int(n1)+int(n2))
