#If-Else and Else-If Conditionals
# var1 = 56
# var2 = int(input())
"""Note: When we use if 'Condition1:
                     'Code1'
and if 'Condition2:
    'Code2'
like this two times, then Compiler checks first if cond then second if cond and then go to else if both if condtions 
are false. This takes more storage in case of there are more if conditionals (like 100-150 if cond) as Compiler 
keeps checking all the if conditionals untill the end and then goes towards else.
Thus for Avoiding this else-if(elif) condtion is used."""
# if var2>var1: # ':' is used to Enter the Conditional
#     print("Greater")
# elif var2== var1:
#     print("Equal")
# else:
#     print("Smaller")

# list1 =[5,6,3]
# print(5 in list1)
# print(25 in list1)
# print(8 not in list1)
# print(6 not in list1)
# if 5 in list1:
#     print("YES its in the List")

"""Quiz: Input an age from user, if the age is 18+ then print "You are eligible to Drive" if not 18+ then print "You
arent eligible to drive" and if the age is 18 then print "SORRY, Cannot Say !!" """
print("Enter your age:")
age = int(input())
if age>18:
    print("You are Eligible to Drive")
elif age== 18:
    print("SORRY, Cannot Say!!")
else:
    print("You are not Eligible to Drive")



