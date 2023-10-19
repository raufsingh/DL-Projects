import numpy
import cv2

img=cv2.imread('D:\\Deep learning\\images1.jpg')
img=cv2.resize(img,(700,400))
#img=cv2.line(img,(0,0),(200,200),(158,190,400),28)
#img=cv2.arrowedLine(img,(0,0),(200,200),(158,190,400),28)
#img=cv2.rectangle(img,(200,100),(250,150),(158,190,400),18)
#img=cv2.circle(img,(400,300),45,(50,200,600),10)
#font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
#img=cv2.putText(img,'Gwalior Fort',(10,120),font,3,(0,125,125),3)
#img=cv2.ellipse(img,(120,100),(100,50),30,0,180,(0,0,255),5)

cv2.imshow('myimage',img)
cv2.waitKey(0)

cv2.destroyAllWindows()