import rhinoscriptsyntax as rs


#mark point numbers
# def mark(self):
#     num = 0
#     for pt in self:
#         rs.AddTextDot(num,pt)
#         num += 1

#draw base frame
def drawFrame(crvList,crv1,crv2,piece):

    #divide crv
    pts1 = rs.DivideCurve(crv1, piece, False, True)
    pts2 = rs.DivideCurve(crv2, piece, False, True)

    for num in range(piece):
        ptsGroup = (pts1[num],pts2[num],pts2[num+1],pts1[num+1],pts1[num]) 
        crvList.append(rs.AddCurve(ptsGroup, 1))
            
#draw curves for each frame
def drawCurves(crvList):
    for crvGUID in crvList:

        #get control points
        pts = rs.CurveEditPoints(crvGUID)
        #get centroid
        centroid = rs.CurveAreaCentroid(crvGUID)[0]

        #draw curves for each 2 points along centoid
        rs.AddCurve((pts[0],centroid,pts[1]),degree=2)
        rs.AddCurve((pts[1],centroid,pts[2]),degree=2)
        rs.AddCurve((pts[2],centroid,pts[3]),degree=2)
        rs.AddCurve((pts[3],centroid,pts[0]),degree=2)

        #draw centrol circle
        rs.ScaleObject(rs.AddCurve(pts), centroid,(.5,.5,.5))


#get 2 crvs
crv1 = rs.GetObject('sel crv1', rs.filter.curve)
crv2 = rs.GetObject('sel crv2', rs.filter.curve)

#draw frame and curvs for each frame
piece = 5
crvList = []
drawFrame(crvList,crv1,crv2,piece)
drawCurves(crvList)


