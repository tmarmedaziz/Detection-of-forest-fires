import cv2
import time
from object_detector import ObjectDetector

od = ObjectDetector()
cap = cv2.VideoCapture(0)
while True:
    start_time = time.time()
    success, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_180) 
    
    x, y, x2, y2 = od.detect(img)
    cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.putText(img,"fps: {}".format(1.0 / (time.time() - start_time)), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0, 255), 2)
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):

       break
