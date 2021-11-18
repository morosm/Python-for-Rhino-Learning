import rhinoscriptsyntax as rs

#input rectangle
crvGUID = rs.GetObject('select a curve',rs.filter.curve)

#find edit points
pts = rs.CurveEditPoints(crvGUID)

print(len(pts))

for pt in pts:
    print(pt)
#find centroid
centroid = rs.CurveAreaCentroid(crvGUID)[0]

#label points
rs.AddTextDot('pt0',pts[0])
rs.AddTextDot('pt1',pts[1])
rs.AddTextDot('pt2',pts[2])
rs.AddTextDot('pt3',pts[3])

###Create Geometry###

#Create Lines
rs.AddCurve((pts[0],centroid,pts[1]),degree=2)
rs.AddCurve((pts[1],centroid,pts[2]),degree=2)
rs.AddCurve((pts[2],centroid,pts[3]),degree=2)
rs.AddCurve((pts[3],centroid,pts[0]),degree=2)

#Create Circle
curve = rs.AddCurve(pts)

#Scale Circle
rs.ScaleObject(curve,centroid,(.5,.5,.5))
