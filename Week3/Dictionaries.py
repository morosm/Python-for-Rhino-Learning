###Debugging###
#SyntaxError
#Logic errors
#Semantic errors

###Dictionary###
#Key cannot be a list
#value can be annything (including lists and dictionaries)
#curly brackets{}

#newDict1 = dict()
#newDict2 = {} 

#extract values as a list
# newDict = {'a':1,'b':2}
# vals = newDict.values()
# print(vals)
# print(type(vals))
# vals = list(vals)
# print(vals)

import rhinoscriptsyntax as rs
dict1 = dict()

for i in range(5):
    for j in range(5):
        x = i * 10
        y = j * 10
        z = 0

        dict1[(i,j)]=(x,y,z)

