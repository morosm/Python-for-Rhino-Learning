import rhinoscriptsyntax as rs

crv1 = rs.GetObject('crv', rs.filter.curve)
#pt1 = rs.GetPoint('pt1')
pt1 = rs.CurveAreaCentroid(crv1)[0]
pt2 = rs.GetPoint('pt2')

translation = pt2 - pt1

rs.MoveObject(crv1, translation)