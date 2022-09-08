""" Exercise-1: Create a dictionary & take input from the user and return the meaning of word from the dictionary"""
d1={"Mutable":"which changes with an frequent amount of time",
    "Strange":"Something different from the usual",
    "Crown":"A Head Adornment",
    "Comrade":"A Friend"}
meaning=(input("Enter the word from dictionary whose meaning you want: "))
print(d1[meaning.capitalize()])
