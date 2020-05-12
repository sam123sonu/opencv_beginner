import cv2
import numpy as np

pic=np.zeros((512,512,3),np.uint8)
cv2.rectangle(pic,(0,0),(400,300),(255,255,255),-1)
pic2=np.zeros((512,512,3),np.uint8)
cv2.rectangle(pic2,(500,0),(200,400),(255,255,255),-1)
cv2.imshow("photo",pic)
cv2.imshow("sam",pic2)
bit_and=cv2.bitwise_and(pic,pic2)  #u can use these names in imshow method to see results.....currently not is given....
bit_or=cv2.bitwise_or(pic,pic2)
bit_xor=cv2.bitwise_xor(pic,pic2)
bit_not=cv2.bitwise_not(pic)
cv2.imshow("result",bit_not)
k=cv2.waitKey(0)
if k==28:
    cv2.destroyAllWindows()
elif k== ord("s"):
     cv2.imwrite("img2.jpg",pic2)
cv2.destroyAllWindows()
