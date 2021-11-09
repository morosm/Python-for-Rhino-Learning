import rhinoscriptsyntax as rs

crv1 = rs.GetObject('This is a curve.', rs.filter.curve)

#pt = rs.GetObject('Pt',rs.filter.point)
#startPt = rs.CurveStartPoint(crv1)
#midPt = rs.CurveMidPoint(crv1)
#endPt = rs.CurveEndPoint(crv1)
#
#print('start point:', startPt)
#print('mid point:', midPt)
#print('end poi

##get curve centroid
#centorid = rs.CurveAreaCentroid(crv1)
#print(centorid)
#
##crv1 = rs.RotateObject(crv1, startPt, 20, None, True)
#crv1 = rs.ScaleObject(crv1, centorid[0], [.5,.8,.8], True)