import rhinoscriptsyntax as rs

ptList = []

#create a matrix
for i in range(10):
    for j in range(10):
        pt = (i*10,j*10,0)
        # rs.AddPoint(pt)
        ptList.append(pt)


# #mark pts
# for i in range(len(ptList)):
#     rs.AddTextDot(i,ptList[i])

# #get a shape and its centroid
# shape = rs.GetObject('sel crv',rs.filter.curve)
# centroid = rs.CurveAreaCentroid(shape)[0]

# #duplicate shape in matrix
# for i in range(len(ptList)):
#     translation = (ptList[i][0]-centroid[0], 
#                     ptList[i][1]-centroid[1], 
#                     ptList[i][2]-centroid[2]   
#                     )
#     shape2 = rs.CopyObject(shape,translation)

#pt attractor
attractor = rs.GetPoint("sel pt")
for i in range(len(ptList)):
    distance = rs.Distance(attractor,ptList[i])
    distance = distance/20

    rs.AddCircle(ptList[i],distance)
    