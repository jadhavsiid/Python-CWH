# How to Import Modules in Python ??
import sklearn as sk
print(sk.__version__) #this will tell version of our module.

import sys
print(sys.path) #this will tell the path from which it is getting the module.

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import File2 # best way to import any variable from any file
print(File2.a)

from File2 import a # not that best way to import any variable from any file
print(a)

File2.joke("This is Python")




