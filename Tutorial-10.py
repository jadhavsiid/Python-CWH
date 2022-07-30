#Dictionaries and its Function
"""Dictionary is nothing but key value pairs"""
# d1 = {} #List is denoted by open-close Curly brackets
# print(type(d1))
d1 = {"Siddhesh":"Burger","Rohan": "Pizza", "Ajay":"Hot Dog","Shubham":{"B":"Maggie","L":"Dal aur roti","D":"Chicken"}}
# print(d1["Siddhesh"]) #This gives Iteam associated with the declared key of dictionary.
# print(d1["Shubham"]) #This Prints Dictionary of any key from the parent dictionary.
# print(d1["Shubham"]["B"]) #This prints the particular Iteam associated with the particular key of the
#                          # dictionary of a particular key of a parent dictionary.
#
# d1["John"]="Junk food" #Dictionary Extension: To add a key in a Dictionary.
# print(d1)
#
# del d1["John"] #To Remove a key from Dictionary.
# print(d1)

#Dictionary Functions
d3=d1.copy() #Creates a copy of one dictionary into another.
del d3["Ajay"]
print(d1)
print(d3)
print(d1.get("Ajay")) #Prints Iteam associated with the declared key of the dictionary.
print(d1.update({"Leena":"Ice Cream"})) #To add an key with its Iteams in an existing dictionary to update it.
print(d1.keys()) #Prints all the keys inside a dictionary.
print(d1.items()) #Prints all the Iteams inside a dictionary.
