import matplotlib.pyplot as plt
import math
import numpy as np
import cv2 as cv

import get_position
pi=math.pi
x=768
y=576




def dis(x1, y1, a, b, c):      
    d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
    return d


def valid(p1,p2,i,k):
    y_=p2[1]-p1[1]
    x_=p2[0]-p1[0]
    angle_=math.atan2(y_,x_)
    if angle_<0:
        angle_+=2*pi
    if angle_<= pi*(i)/(k) :
        if angle_>= pi*(i-1)/(k):
            return 1
    return 0





k = int(input("Enter k between five and fifteen: ") )
    
clk=get_position.mouse_pos()
n=len(clk)

img = np.zeros([y,x,3],dtype=np.uint8)
img.fill(255)


slope=[]
for i in range(1,k+1):
    slope.append(math.tan(pi*(2*i-1)/(2*k)))

lines=[]
for pnt in clk:
    for m in slope:
        a=-m
        b=1
        c=m*pnt[1][0]-(pnt[1][1])
        lines.append([pnt[0],a,b,c])
        

graph=[]


for pnt in clk:   
    i=0
    for line in lines:
        distance=[]
        if line[0]==pnt[0]:
            i+=1
            for row in clk:
                if row[0]!=pnt[0]:
                    if valid(pnt[1],row[1],i,k):
                        d=dis(row[1][0],row[1][1],line[1],line[2],line[3])
                        distance.append([pnt[0],row[0],d])
            distance.sort(key=lambda s:s[2])          
            try:
                graph.append([distance[0][0],distance[0][1]])   
            except:
                pass
            



            

for row in graph:
    for pnt in clk:
        if row[0]==pnt[0]:
            start_point=pnt[1]
        if row[1]==pnt[0]:
            end_point=pnt[1]    
    img = cv.line(img, start_point, end_point, (0, 255, 0) , 1)

for row in clk:
    img=cv.circle(img,(row[1][0],row[1][1]), 3, (0,0,255), 2)
        
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows() 