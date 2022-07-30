# Writing and Appending to a file

# f = open("Siddhesh.txt", "w") #First Erase whatever it is in a file and then write
# f.write("Siddhesh launda Sexy hai !\n")

# f = open("Siddhesh.txt", "a")
# a = f.write("Siddhesh launda Sexy hai !\n") #Doesn't Erase whatever it is in a file but it keeps writing.
# print(a) #Gives the number of Characters in a file.
# f.close()

# Handle read and write both
f = open("Siddhesh.txt","r+")
print(f.read())
f.write("Thank you!")
f.close()