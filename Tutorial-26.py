# File Io: open(), read() & readline()
f = open("siddhesh.txt","rt")

print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())

# content = f.read(34454)
# print("1",content)

# content = f.read(34454)
# print("2",content)

# for line in f:
#     print(line, end="")

f.close()
