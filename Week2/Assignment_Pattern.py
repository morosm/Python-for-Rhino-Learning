import rhinoscriptsyntax as rs
import random as rnd

#input matrix 
num = int(input("input x for matrix x*x"))

#side number of the circle
side = rnd.randint(5,10)
print('side number :',side)

#create pt list for matrix
ptList1 = []
for i in range(num):
    for j in range(num):
        pt = (i,j,0)
        ptList1.append(pt)

#create a circle inside the matrix
radius = i/2
centriod = (radius,radius,0)
circle = rs.AddCircle(centriod,radius)
rs.HideObject(circle)

#pt list2 :get points from the circle as attractors
ptList2 = rs.DivideCurve(circle, side, False, True)

#get the distance between pt and attractor
distanceList = []
for i in range(len(ptList1)):
    attractor = ptList2[i%side]
    distance = rs.Distance(ptList1[i],attractor)
    distanceList.append(distance)

#regenerate the distanc10e
denominator = max(distanceList)
distanceList = [i/denominator/2 for i in distanceList]

#draw circles
for i in range(len(ptList1)):
    rs.AddCircle(ptList1[i],distanceList[i])