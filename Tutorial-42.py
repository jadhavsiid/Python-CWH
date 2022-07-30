# Time Module in python
import time
initial = time.time() #importing function from a time module to find time and store it in initial variable.
# print(initial)
k = 0
while(k<3):
    print("Hello Siddhesh")
    time.sleep(2) #used to halt compiler for declared seconds.
    k+=1
print("While Loop ran in ",time.time()-initial,"seconds") #this will minus time.time() with inital time.time()
initial2 = time.time() #storing function from time module in another variable.
for i in range(3):
    print("Hello Sid")
print("For Loop ran in", time.time()-initial2,"seconds") #this will minus time.time() with inital2 time.time()

localtime= time.asctime(time.localtime(time.time()))
print(localtime)



