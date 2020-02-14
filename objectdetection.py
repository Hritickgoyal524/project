import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
large=[]
forcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("output.avi",forcc,20.0,(640,480))#it contain 4 argument 1.filenae to store2.forcc code 3.framepersecond,size
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while(True):
     _, frame=cap.read()
     blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
     hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
     lh=cv2.getTrackbarPos("LH","Tracking")
     ls=cv2.getTrackbarPos("LS","Tracking")
     lv=cv2.getTrackbarPos("LV","Tracking")
     
     uh=cv2.getTrackbarPos("UH","Tracking")
     us=cv2.getTrackbarPos("US","Tracking")
     uv=cv2.getTrackbarPos("UV","Tracking")
     l_b=np.array([lh,ls,lv])
     u_b=np.array([uh,us,uv])
     print((lh,ls,lv))
     print((uh,us,uv))
     mask=cv2.inRange(hsv,l_b,u_b)

     res=cv2.bitwise_and(frame,frame,mask=mask)

     countours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     max_area = 0
     max_index = 0
     for i, contour in enumerate(countours):
        area = cv2.contourArea(contour)
        if max_area < area:
            max_area = area
            max_index = i   
     (x,y,w,h) = cv2.boundingRect(countours[max_index]) 
     cv2.rectangle(res, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.drawContours(res, countours[max_index], -1, (0, 255, 0), 3)
     out.write(res)
     cv2.imshow("frame",frame)
     cv2.imshow("mask",mask)
     cv2.imshow("result",res)
     key=cv2.waitKey(1)
     if key==27:
         break
cap.release()
cv2.destroyAllWindows()

