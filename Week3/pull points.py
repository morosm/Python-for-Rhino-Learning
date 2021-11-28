#PULLED POINT FUNCTION EXAMPLE
import rhinoscriptsyntax as rs
import random as rnd


def PointMatrix(IMAX,JMAX):
    #create an empty list
    ptDict = dict()
    crvList = list()
    val01 = 0
    val02 = IMAX * JMAX

    #increment loop to generate points
    for i in range(IMAX):
        for j in range(JMAX):
            #define x in terms of i
            #define y in terms of j
            x = i*5
            y = j*5
            z = 0

            #render point in rhinospace
            rs.AddPoint(x,y,z)

            #save point values in ditionary
            ptDict[(i,j)] = (x,y,z)
    
    #loop through dictionary to create geometry
    for i in range(IMAX):
        for j in range(JMAX):
            if i > 0 and j > 0:
                newPt = PullPt(ptDict[i-1,j-1],ptDict[i,j], val01, val02)
                rs.AddCurve((ptDict[i-1,j], newPt, ptDict[i,j-1]))
                val01 = val01 + 1
    
def PullPt(PT01,PT02,VAL01,VAL02):
    #clear all data being held in point variable
    point = None
    #calculate pulled point
    point = ((PT01[0]*VAL01+PT02[0]*VAL02)/(VAL01+VAL02),
            (PT01[1]*VAL01+PT02[1]*VAL02)/(VAL01+VAL02),
            (PT01[2]*VAL01+PT02[2]*VAL02)/(VAL01+VAL02))
    #return pulled point
    return point

def main():
    #input values for imax and jmax
    imax = 10
    jmax = 10

    #call PointMatrix() funtion
    PointMatrix(imax, jmax)

main()
    
