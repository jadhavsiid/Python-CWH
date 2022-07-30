# For Loops in Python
list1 = {"Siddhesh","Shubham","Pavan","Ananya"}
for item in list1:
    print(item)

list2 = [["Siddhesh",1],["Shubham",2],["Pavan",3],["Ananya",5]]
for item,lollipop in list2:
    print(item,"and lollipop is", lollipop)

dict1 = dict(list2)
print(dict1)
for item,lollipop in dict1.items():
    print(item,"and lollipop is", lollipop)

for item in dict1:
    print(item)

"""Quiz: Prepare a list Consisting of Heterogeneous Items. Check whether the Item is a number, if it is a number
than check whether it is greater than, 6 if it is greater than 6 then Print it."""
# items = {int,float,"Siddhesh",25,30,45,6,8,}
# for item in items:
#     if str(item).isnumeric() and item>6:
#         print(item)


