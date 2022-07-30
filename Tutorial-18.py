# Break and Continue
# i=0
# while(True):
#     if i+1 < 5:
#         i = i + 1
#         continue
#
#     print(i+1)
#     if (i==44):
#         break #Stop the Loop
#     i = i + 1

"""Quiz: Take input from user until he gives the input as number > 100."""
while(True):
    a = int(input("Enter a number:"))
    if(a>100):
        print("YEAH!! You've Entered a number greater than 100")
        break
    else:
        print("Try Again Dear!")
        continue