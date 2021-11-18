#Bone Structure Three
import rhinoscriptsyntax as rs
import random as rnd

#input a point
ptGUID = rs.GetObject('sel a point', rs.filter.point)

#randomly generate circle radius
radius = rnd.randint(5,15)
print(radius)

#draw a circle using point as origin
circle = rs.AddCircle(ptGUID, radius)
rs.HideObject(circle)

#divide circle - save points in a list
pts1 = rs.DivideCurve(circle,10,False,True)

#shift list of pts for 1
pts2 = list(pts1)
pts2.append(pts2.pop(0))

# #lable points
# counter = 0
# for pt in pts1:
#     rs.AddTextDot(str(counter),pt)
#     counter += 1

#draw curves
for i in range(len(pts1)):
    print(i)
    rs.AddCurve((ptGUID,pts1[i],pts2[i],ptGUID))


