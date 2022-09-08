#Python Lists and Lists Functions
grocery = ["Harpic","vim bar","deodrant","Bhindi","Lollipop",56] #Classic example of list.
#Listing
# print(grocery) #Print's the whole list of Iteams.
# print(grocery[0]) #prints the iteam of the list on the given index.
# print(grocery[1]) #prints the iteam of the list on the given index.
# print(grocery[2]) #prints the iteam of the list on the given index.
# print(grocery[3]) #prints the iteam of the list on the given index.
# print(grocery[4]) #prints the iteam of the list on the given index.
# print(grocery[5],'\n') #prints the iteam of the list on the given index.
numbers = [91,52, 86, 77]
# print(numbers) #Print's the whole list of numbers.
# print(min(numbers)) #Prints the smallest number in the list.
# print(max(numbers)) #Prints the largest numberin the list.
# print(numbers[2],'\n') #prints the number on the list of the given index.
#List Functions:
# numbers.append(21) #This adds the number which is bieng input by user at the end of the list.
# print(numbers)
#
# numbers.insert(2,96) #This adds the number which is bieng input by user at the user specified index.
# print(numbers)
#
# numbers.remove(77) #Removes the desired number from the list.
# print(numbers)
#
# numbers.pop() #Removes the last element in the list.
# print(numbers)
#
# numbers[1]=98 #Changes the value of the mentioned index by adding new mentioned value.
# print(numbers)
#
# numbers.sort() #Sort all the numbers in the list in ascending order.
# print(numbers)
#
# numbers.reverse() #Sorts all the numbers in the list in descending order.
# print(numbers)

#list Slicing
# print(numbers[0:5]) #To Print the list starting from declared initialised and terminating index
# print(numbers[:5]) #Does the same job even initialised index is not mentioned.
# print(numbers[:]) #Does the same job even initialised and terminating index isn't mentioned.
# print(numbers[1:],'\n') #Skips the element on first index of the list and print it.

#Extended Slicing
# print(numbers[::]) #Prints the Complete list.
# print(numbers[::2]) #Prints Alternate numbers in the list.
# print(numbers[::3]) #Skips two numbers in the list and print it.
# print(numbers[::-1]) #Inverts the list and prints it.

#Tupling
"""Remember: Mutable = can change.
             Immutable = cannot change."""
# tp=(1,2,3) #classic example of tuple.
# print(tp)
"""Note: Lists are shown in square brackets and Tuple are shown in open close parenthesis."""
# tp[1]= 8 # Will give error as in tuple values cannot be changed in such way by as they can in list.
# print(tp)
"""Thus we may say that lists are Mutable and Tuple's are Immutable."""

# tp1=(1) #This will not print open-close parenthesis while printing the tuple as it has single element in it.
# print(tp1)
#
# tp2=(1,) #This will print open-close parenthesis while printing the tuple eventough it has single element.
# print(tp2)

# How to swap two numbers (Normally)
a=1
b=10
temp = a
a = b
b = temp
print("The value of a is:",a)
print("The value of b is:",b,'\n')

# How to swap two numbers (Python Special 😎)
a = 80
b = 50
a,b = b,a
print("The value of a is:",a)
print("The value of b is:",b)