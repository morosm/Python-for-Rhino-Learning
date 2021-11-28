import rhinoscriptsyntax as rs
import random as rnd

imax = 10
jmax = 10
gap = 10
ptDicts = dict()

#generate matrix
for i in range(imax):
    for j in range(jmax):
        x = i * gap + rnd.random()
        y = j * gap + rnd.random()
        z = 0
        ptDicts[(i,j)]=(x,y,z)


#draw pattern
for i in range(imax):
    for j in range(jmax):
        if i>0 and j>0:
            #get the centroid
            frame = rs.AddCurve((ptDicts[i,j],ptDicts[i-1,j],ptDicts[i-1,j-1],ptDicts[i,j-1],ptDicts[i,j]),1)
            rs.HideObject(frame)
            cenroid = rs.CurveAreaCentroid(frame)[0]

            #get midpoints of each side
            midTop = (ptDicts[i,j][0]/2+ptDicts[i-1,j][0]/2,
                    ptDicts[i,j][1]/2+ptDicts[i-1,j][1]/2,
                    ptDicts[i,j][2]/2+ptDicts[i-1,j][2]/2)
            midLeft = (ptDicts[i-1,j][0]/2+ptDicts[i-1,j-1][0]/2,
                    ptDicts[i-1,j][1]/2+ptDicts[i-1,j-1][1]/2,
                    ptDicts[i-1,j][2]/2+ptDicts[i-1,j-1][2]/2)
            midBottom = (ptDicts[i-1,j-1][0]/2+ptDicts[i,j-1][0]/2,
                    ptDicts[i-1,j-1][1]/2+ptDicts[i,j-1][1]/2,
                    ptDicts[i-1,j-1][2]/2+ptDicts[i,j-1][2]/2)
            midRight = (ptDicts[i,j-1][0]/2+ptDicts[i,j][0]/2,
                    ptDicts[i,j-1][1]/2+ptDicts[i,j][1]/2,
                    ptDicts[i,j-1][2]/2+ptDicts[i,j][2]/2)
                    
            #draw curves
            crv1 = rs.AddCurve((midTop,cenroid,midLeft),3)
            crv2 = rs.AddCurve((midLeft,cenroid,midBottom),3)
            crv3 = rs.AddCurve((midBottom,cenroid,midRight),3)
            crv4 = rs.AddCurve((midRight,cenroid,midTop),3)

            #draw central circle
            rs.AddCurve((rs.CurveMidPoint(crv1),
                        rs.CurveMidPoint(crv2),
                        rs.CurveMidPoint(crv3),
                        rs.CurveMidPoint(crv4),
                        rs.CurveMidPoint(crv1)),   
                        3)
