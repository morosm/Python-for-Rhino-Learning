import rhinoscriptsyntax as rs
import random as rnd

#get a point
centorid = rs.AddPoint((0,0,0))

#generate a random radius
radius = rnd.randint(10,20)

#draw a circle
circle = rs.AddCircle(centorid,radius)

#divide the circle
pts = rs.DivideCurve(circle,10,False,True)

#draw lines and midpoints on lines
lines = []
midPoints = []

for pt in pts:
       line = rs.AddLine(centorid,pt)

       #hide lines
       rs.HideObject(line)

       lines.append(line)
       midPoint = rs.CurveMidPoint(line)
       midPoints.append(midPoint)

#shift midpoint       
midPoints.append(midPoints.pop(0))

#draw curves
for i in range(len(lines)):
       rs.AddCurve((pts[i],midPoints[i],centorid),3)

#hide centorid and circle
rs.HideObject(centorid)
rs.HideObject(circle)