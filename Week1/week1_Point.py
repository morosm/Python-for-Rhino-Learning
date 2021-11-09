import rhinoscriptsyntax as rs

crvID = rs.GetObject('Get a curve', filter = rs.filter.curve)

point1 = rs.GetObject('Get Point1',filter = rs.filter.point)
point2 = rs.GetObject('Get Point2', filter = rs.filter.point)

point1 = rs.PointCoordinates(point1)
point2 = rs.PointCoordinates(point2)

translation = point2 - point1

print(translation)

#rs.MoveObject(crvID, translation)
rs.CopyObject(crvID, translation)