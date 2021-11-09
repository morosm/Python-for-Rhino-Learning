import rhinoscriptsyntax as rs

#get geometry and curve path
geo = rs.GetObject('geo',rs.filter.curve)
crv = rs.GetObject('crv',rs.filter.curve)

#divide curve points
ptList = rs.DivideCurve(crv,50)

#run for each point on curve
for pt in ptList:
    centroid = rs.CurveAreaCentroid(geo)[0]
    translation = pt - centroid
    geo = rs.CopyObject(geo, translation)
    
    centroid = rs.CurveAreaCentroid(geo)[0]
    geo = rs.RotateObject(geo, centroid, 15, None, False)
    geo = rs.ScaleObject(geo, centroid, [.90,.8,.8], False)