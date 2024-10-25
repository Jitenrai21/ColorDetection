import cv2
from util import get_limits
from PIL import Image

yellow = [0,255,255] # yellow in BGR colorspace
cap = cv2.VideoCapture(0) #how many webcams you have connected

while True:
    ret, frame = cap.read()

    hsvImage =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask) #converting numpy array into pillow

    bbox = mask_.getbbox() #for the bounding box of the object

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    cv2.imshow('mask', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()