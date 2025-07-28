import cv2
import pandas
from datetime import datetime


first_frame = None

df = pandas.DataFrame(columns=["Start","End"])

status_list=[None,None]
times =[]

video = cv2.VideoCapture(0)


while True:
    
    status=0
    
    check,video_frame = video.read()
    gray = cv2.cvtColor(video_frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(41,41),0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    #absdiff: Computes the absolute difference between the current frame and the background.
    #This highlights areas where movement occurred.
    #threshold: Converts the difference to black & white.
    #Pixels with value > 30 become white (255), else black (0).
    #[1] selects the actual thresholded image (OpenCV returns a tuple).
    #dilate: Fills small holes and connects white regions to make contours more detectable.
    #iterations=2 makes dilation stronger.
    
    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame,60,255,cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame,None,iterations=1)
    
    #Finds the outlines of moving objects (contours).
    #RETR_EXTERNAL: Retrieves only outer contours (ignores nested).
    #CHAIN_APPROX_SIMPLE: Compresses contour points to save memory.
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 10000: #ignor small movements
            continue
        
        #these two will only run when subject greater than 100x100px
        status = 1
        (x,y,h,w) = cv2.boundingRect(contour)
        cv2.rectangle(video_frame,(x,y),(x+w,y+h),(0,255,0),3) #adds rectangle to actual frame

    #Status update time section:
    status_list =status_list[-2:] #for memory only last 2 elements
    status_list.append(status)
    if (status_list[-1]==1) and (status_list[-2]==0):
        times.append(datetime.now())
        
    if (status_list[-1]==0) and (status_list[-2]==1):
        times.append(datetime.now())
        
    # Show live camera and processed frames
    #cv2.imshow("Gray_frame",gray)
    #cv2.imshow("delta_frame",delta_frame)
    #cv2.imshow("thresh_frame",thresh_frame)
    cv2.imshow("color_frame",video_frame)
    
    keys = cv2.waitKey(1)
    if keys == ord('q'):
        
        #this will append datetime when i exit the program when i was in the frame
        if status == 1:
            times.append(datetime.now())
        break
    
#Storing start and end times in dataframe:
    
rows = []
for i in range(0, len(times), 2):
    rows.append({"Start": times[i], "End": times[i+1]})

df = pandas.DataFrame(rows)





df.to_csv("TimeStamps.csv")
print(status_list)
#print(times)
video.release()
cv2.destroyAllWindows()