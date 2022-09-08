# *args and **kwargs in Python
def function_name_print(a,b,c,d):
    print(a,b,c,d)
def funargs(normal,*args,**kwargs): #Defining *args [Note: normal argument should always be defined first]
    print(normal)
    for item in args:
        print(item)
    print("Here is the food item liked by each of the person:")
    for key,value in kwargs.items():
        print(f"{key} likes {value}")
    """print(args[0]) #will print a string on 0th index of a declared list in a function.
    print(args[2]) #will print a string on 2nd index of a declared list in a function.
    print(type(args)) #this will always print type as tuple as it is just a convention."""

# function_name_print("Harshada","Bhakti","Devendra","Siddhesh")
sid = ["Harshada","Bhakti","Devendra","Siddhesh","Ananya"] #preparing a list to declare inside function.
kw= {"Siddhesh":"Burger","Rohan": "Pizza", "Ajay":"Hot Dog","Pandu":"Paani Puri"}
funargs(*sid) #declaring a *args Function.
normal = 34
funargs(normal,*sid)
funargs(normal,*sid,**kw)



