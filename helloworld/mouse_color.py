import cv2
import numpy as np
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue = pic[y,x,0]
        green= pic[y,x,1]
        red= pic[y,x,2]
        img =np.zeros((512,512,3),np.uint8)
        img[:]=[blue,green,red]
        cv2.imshow("color", img)


pic=cv2.imread("butterfly.jpg",1)
count=[]
cv2.imshow("photo",pic)
cv2.setMouseCallback("photo",click_event)
k=cv2.waitKey(0)
if k==28:
    cv2.destroyAllWindows()
elif k== ord("s"):
     cv2.imwrite("but_copy.png",pic)
cv2.destroyAllWindows()
