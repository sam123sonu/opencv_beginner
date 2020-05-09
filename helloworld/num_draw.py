import numpy as np
import cv2
img=np.zeros((600,600,3),np.uint8)   #here we are creating screen(black array )using numpy library
print(img)
img=cv2.line(img,(0,0),(200,200),(0,255,0),6)
img=cv2.arrowedLine(img,(0,200),(200,200),(255,0,0),8)
img=cv2.rectangle(img,(510,0),(300,200),(0,0,255),10)
img=cv2.circle(img,(405,100),100,(255,0,255),-1)
font_style=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'python',(40,560),font_style,4,(255,255,0),6,cv2.LINE_8)
cv2.imshow('sam',img)
cv2.waitKey(0)
cv2.destroyAllWindows()