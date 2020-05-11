import cv2
import numpy as np


img=cv2.imread("messi.jpg",1)

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img=cv2.merge((b,g,r))

#f_ball=img[280:340,330:390]
#by commenting middle one and opening 2 commented line will copy ball
img[280:340,330:390]=img[273:333,100:160]
#img[273:333,100:160]=f_ball

cv2.imshow('image',img)
k=cv2.waitKey(0)

cv2.destroyAllWindows()
