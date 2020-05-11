import cv2
import numpy as np
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(pic,(x,y),3,(0,0,255),-1,cv2.LINE_AA)

        count.append((x,y))
        if len(count)>=2:
            cv2.line(pic,count[-1],count[-2],(255,255,255),2)
        cv2.imshow("photo", pic)

pic = np.zeros((512,512,3),np.uint8)
#pic=cv2.imread("butterfly.jpg",1)
count=[]
cv2.imshow("photo",pic)
cv2.setMouseCallback("photo",click_event)
k=cv2.waitKey(0)
if k==28:
    cv2.destroyAllWindows()
elif k== ord("s"):
     cv2.imwrite("but_copy.png",pic)
cv2.destroyAllWindows()
