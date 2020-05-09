import cv2

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(cap.get(3))
print(cap.get(4))

fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('capture.avi',fourcc,20.0,(640,480))

print(cap.isOpened())
while(cap.isOpened()):
   ret,frame=cap.read()
   if ret==True:
       font=cv2.FONT_HERSHEY_SIMPLEX
       text="width:"+str(cap.get(3))+"               height:"+str(cap.get(4))
       cv2.putText(frame,text,(10,50),font,1,(255,255,255),2,cv2.LINE_AA)
       out.write(frame)

       cv2.imshow("sam",frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
   else:
       break
cap.release()
cv2.destroyAllWindows()

