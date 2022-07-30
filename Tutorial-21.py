# Operators in Python
""" Types of Operators in Python
1.) Arithmetic Operators.
2.) Assignment Operator.
3.) Comparison Operator.
4.) Logical Operators.
5.) Identity Operators.
6.) Membership Operators.
7.) Bitwise Operators."""

print("Arithmetic Operators")
print("5+6 is =",5+6)
print("5-6 is =",5-6)
print("5*6 is =",5*6)
print("5**6 is =",5**6) #Exponential Operator
print("5/6 is =",5/6)
print("15//6 is =",15//6) #Double divide operator
print("5%6 is =",5%6,'\n')

print("Assignment Operators")
a = 5
print(a)
a += 7
print(a)
a /= 4
print(a,'\n')

print("Comparison Operators")
i =8
print(i == 5)
print(i>8)
print(i>=8,)
print(i<=8,'\n')

print("Logical Operators")
a = True
b = False
print(a and b)
print(a or b,'\n')

print("Identity Operators")
print(a is b)
print(a is not b)
print(5 is not 7,'\n')

print("Membership Operators")
list= {3,3,2,35,31,39,32}
print(32 in list)
print(24 in list)
print(24 not in list,'\n')

print("Bitwise Opearators")
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
print(0 & 1)
print(0 | 1)
print(0 | 3)

