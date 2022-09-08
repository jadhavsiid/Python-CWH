# String Slicing and Other Functions in Python
mystr = "siddhesh is a good boy."
print(mystr) #This will print a complete String.
print(mystr[4]) #To Print a Letter on index 4 of mystr.
print(mystr[0:4]) #To Print Letters of mystr uptill index 4 excluding the letter on 4th index.
print(len(mystr)) #To print Length of a String.
#print(mystr[78]) # This will give error as the length of complete string is 22.
print(mystr[0:78],'\n') #It gives Complete String rather than giving a error.

# Advance Slicing
print(mystr[0:7:2]) #This will print every alternate letter of the string from declared starting and ending index.
print(mystr[::3]) #This will start skipping 2-2 characters.
print(mystr[::100]) #This will take default index as the termination limit exceeds the length of the string.
print(mystr[0:]) #This will print the complete string.
print(mystr[:8]) #This will consdier zero by itself and will print the string uptill the terminating index is declared.
print(mystr[::],'\n') #"""This will also print the complete string as it will itself consider zero at beginning and the
                 #last index at the termination."""
# Negative indices
print(mystr[-4:]) #It considers indices from the Right side of the String.
print(mystr[-4:-2]) #This will print every alternate letter of the string from right side of declared starting and
                    # ending index.
print(mystr[18:22]) #Positive way of declaring line 19.
print(mystr[-4::-1],'\n') #To invert the String leaving the first negatively declared part.

#String Functions
print(mystr.isalnum())#"""Returns Boolean variavles for now it is returning false because current string isn't
                      #alphanumeric"""
print(mystr.isalpha()) #It will check whether the string is Alpha.
print(mystr.endswith("boy"))#"""It will check whether the string is ending with the word mentioned and will return true
print(mystr.endswith("bdoy")) #if the string is ending with the same."""
print(mystr.count("d")) #Returns the number uptill which the declared word is repeated.
print(mystr.capitalize()) #Capitalise the word on 0th index of the String.
print(mystr.find("is")) #Returns the index number of the entered word to find it in the string.
print(mystr.lower()) #Decapitalize the whole String.
print(mystr.upper()) #Capitalize the whole String.
print(mystr.replace("is","are"),'\n') #Replaces one String with another.
