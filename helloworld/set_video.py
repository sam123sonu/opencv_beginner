import cv2

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 400)    #here we are setting the width of the frame
cap.set(4, 400)    #here we are setting the height of the frame

print(cap.get(3))
print(cap.get(4))

fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('capture.avi',fourcc,20.0,(640,480))

print(cap.isOpened())
while(cap.isOpened()):
   ret,frame=cap.read()
   if ret==True:
      out.write(frame)
      grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      cv2.imshow("sam",grey)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
   else:
       break
cap.release()
cv2.destroyAllWindows()

