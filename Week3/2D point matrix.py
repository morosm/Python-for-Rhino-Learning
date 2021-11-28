from rhinoscript.layer import ParentLayer
import rhinoscriptsyntax as rs
import random as rnd

ptDict = dict()
imax = 10
jmax = 10

#generate ptDict
for i in range(imax):
    for j in range(jmax):
        x = i + i**2 #+ rnd.random()*3
        y = j + j**2 #+ rnd.random()*3
        z = 0
        #render point in rhinospace'
        rs.AddPoint(x,y,z)
        #save point in dict
        ptDict[(i,j)] = (x,y,z)

#loop through dict
for i in range(imax):
    for j in range(jmax):
        # #print out point values with (i,j) key assignments
        # print(i,j,':',ptDict[(i,j)])
        ## label points in rhinospace with (i,j) key assignments
        # rs.AddTextDot((i,j),ptDict[(i,j)])
        
        #create closed 3 degree curve using all four points
        if i>0 and j>0:
            rs.AddCurve((ptDict[i,j],ptDict[i-1,j],
                        ptDict[i-1,j-1],ptDict[i,j-1],
                        ptDict[i,j]),3)
            