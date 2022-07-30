# Scope, Global variables and keywords
l=10 #Global variable.
def function1(n):
    # l=5 #Local variable.
    m=8 #Local variable.
    # l = l+45 # This will throw error if l=5 is commented since l=10 cannot be further changed as global variables are
                                                                                                           # read only.
    global l #This activate global variable inside the scope.
    l = l + 45  #This will make the change happen inside only if l inside scope is commented.
    print(l)
    print(n, "I have Printed!")
    print(l,m)
function1("This is me.")
print(l)
# print(m) # This will throw error bcoz the variable m i declared inside scope and is a global variable.

# Global variable in Nested Functions
x = 89 #
def siddhesh():
    x = 20
    def harshada():
        global x #This will not change value of x bcoz it will try to check upwards for x which will be not there.
        x = 88
    print("before calling Harshada():",x)
    harshada()
    print("after calling Harshada():",x)
siddhesh()
print(x)
