# seek(),tell() & more on Python files

f = open("Siddhesh.txt")
# print(f.tell()) #tells us location of file pointer
print(f.readline())
# print(f.tell())
print(f.seek(10)) #to bring file pointer on a specific location
print(f.readline())
# print(f.tell())
f.close()