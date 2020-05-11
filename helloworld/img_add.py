import cv2
import numpy as np


img=cv2.imread("messi.jpg",1)
img2=cv2.imread("chessboard.png",1)

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img=cv2.merge((b,g,r))
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
main=cv2.addWeighted(img,0.8,img2,0.2,0)#result will be shown acording to the weight of the image we have given..
#main=cv2.add(img,img2)#in this add() function we dont need to put weight.....result given(messi_add.jpg)
cv2.imshow('image',main)
k=cv2.waitKey(0)
if(k==ord('s')):
    cv2.imwrite("messi_addweighted.jpg",main)
cv2.destroyAllWindows()
