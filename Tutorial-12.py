#Sets in Python
# s=set()
# print(type(s))
# S1= {1, 2, 3, 4} #Classic Example of Set.
# print(S1)
# S2= set([9,10,11,12]) #Another Classic Example of declaring a Set.
# print(S2)

#How to add elements in Set
p=set()
# p.add(1) #This is used to add elements in set.
# # p.add(1) this will not print 1 once again as 1 is already printed with previous set & set only returns unique value.
# p.add(2)
# print(p)
# Few Functions of Set
p.union([1,2])
print(p)
p1=p.union([1,2,3])
print(p,p1) #Gives Union of two Set.
p2=p.intersection([1,3])
print(p,p2) #Gives Intersection of two Set.
print(len(p)) #Gives length of a set.
print(max(p1)) #Gives Maximum number from a set p1.
print(p.isdisjoint(p1)) #Tells wheather two sets are disjoint or not.
p.remove(1) #To remove any Element from set.
print(p)
