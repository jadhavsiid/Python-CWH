# F-Strings and String Formatting in Python
import math
me = "Siddhesh"
a1 = 3
# a = "this is %s"%(me,a1)
z = "this is {} {}"
b = z.format(me,a1)
# print(a)
print(b)

a = f"this is {me} {a1} {4*65} {math.cos(30)}" #F-string
print(a)
