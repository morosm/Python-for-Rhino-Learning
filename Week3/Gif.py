import rhinoscriptsyntax as rs
import random as rnd



#generate matrix
def generate_matrix(imax, jmax, frame):
    ptDicts = dict()
    for i in range(imax):
        for j in range(jmax):
            x = i * gap + rnd.random()*frame/4
            y = j * gap + rnd.random()*frame/4
            z = 0
            ptDicts[(i,j)]=(x,y,z)
    return(ptDicts)

    
#draw pattern
def draw_pattern(imax, jmax, ptDicts):
    
    #crv list
    crvList = list()

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
                crv5 = rs.AddCurve((rs.CurveMidPoint(crv1),
                                rs.CurveMidPoint(crv2),
                                rs.CurveMidPoint(crv3),
                                rs.CurveMidPoint(crv4),
                                rs.CurveMidPoint(crv1)),   
                                3)
                crvList.extend([crv1, crv2, crv3, crv4, crv5])
    return(crvList)

def render_step(render_folder, sequence_num):
    file_name = str(int(sequence_num)).zfill(3)
    file_path = " " + render_folder + file_name + ".png"
    rs.Command("_-ViewCaptureToFile" + file_path + " _Enter")
    print(file_path)

#main
def main(imax, jmax, frames, render_folder):

    for frame in range(frames):
        #draw pattern
        ptDicts = generate_matrix(imax, jmax, frame)
        crvList = draw_pattern(imax, jmax, ptDicts)

        #screenshots
        render_step(render_folder, sequence_num = frame)

        #delete crvs
        rs.DeleteObjects(crvList)
    

imax = 10
jmax = 10
frames = 48
render_folder = "E:\\GitHub\\Python-for-Rhino-Learning\\Week3\\Frames\\"
main(imax, jmax, frames, render_folder)