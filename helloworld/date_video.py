import cv2
import datetime
cap=cv2.VideoCapture(0)

print(cap.isOpened())
while(cap.isOpened()):
   ret,frame=cap.read()
   if ret==True:
      print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
      print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

      font=cv2.FONT_HERSHEY_SIMPLEX
      date_time=str(datetime.datetime.now())

      cv2.putText(frame,date_time,(10,20),font,1,(255,255,255),2,cv2.LINE_AA)

      cv2.imshow("sam",frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
   else:
       break
cap.release()
cv2.destroyAllWindows()

