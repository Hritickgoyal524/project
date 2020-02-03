import cv2
cap=cv2.VideoCapture(0)
forcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("output.avi",forcc,20.0,(640,480))#it contain 4 argument 1.filenae to store2.forcc code 3.framepersecond,size
while(cap.isOpened()):
   ret,frame=cap.read()#here ret store true or false while frae store frames of pic
   if ret==True:
      out.write(frame)
      cv2.imshow("frame",frame)
      if cv2.waitKey(1)& 0xFF==ord('q'):#for quiting the procees
         break
   else:
       break
cap.release()
out.release()
cv2.destroyAllWindows()





