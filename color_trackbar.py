import cv2
import numpy as np

def nothing(x):
    print(x)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("sam")

cv2.createTrackbar('B',"sam",0,255,nothing)
cv2.createTrackbar('G',"sam",0,255,nothing)
cv2.createTrackbar('R',"sam",0,255,nothing)


while(1):
  cv2.imshow("sam", img)
  k=cv2.waitKey(1)
  if k==27:
      break
  b=cv2.getTrackbarPos('B','sam')
  g=cv2.getTrackbarPos('G','sam')
  r=cv2.getTrackbarPos('R','sam')

  img[:]=[b,g,r]
  if k==ord('s'):
      cv2.imwrite("bgr.jpg",img)
cv2.destroyAllWindows()
