#DATA TYPES
import rhinoscriptsyntax as rs

#Integer
intX = rs.GetInteger('input integer' , 5)

#Float
num = rs.GetReal('input a number', 5.345)

#String
strVal = "fortyfive cats"

#Boolean
bln01 = True
bln02 = False

#GUID
obj = rs.GetObject('select a box', rs.filter.polysurface)
imnotacurve = rs.GetObject('select a curve', rs.filter.curve)
srf = rs.GetObject('select a surface', rs.filter.surface)

#3D Point
point = rs.GetPoint('select a point')

#OUTPUT
print(intX)
print(num)
print(strVal)
print(bln01)
print(obj)
print(imnotacurve)
print(srf)
print(point)

print type(intX)
print type(num)
print type(strVal)
print type(bln01)
print type(obj)
print type(imnotacurve)
print type(srf) 
