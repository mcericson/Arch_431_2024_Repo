# r: opencv-python
import cv2
from scriptcontext import escape_test

cap = cv2.VideoCapture(0)

output = []
while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()