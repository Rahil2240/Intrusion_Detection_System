import cv2
import send
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   
cap.set(3, 640)  #width 
cap.set(4, 480)  #height

l = []
flag = True   

detector = PoseDetector()

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()   
    if not ret:
        print("Error: Failed to grab frame.")
        break

    frame = detector.findPose(frame) 
    img_list, bbox = detector.findPosition(frame)  

    # Human detection logic
    if len(img_list) > 0:  
        print("Human Detected")
        l.append(1)

    if len(l) > 50 and flag:
        flag = False
        send.sendSms()   

    # Display the frame with pose detection
    cv2.imshow("Pose Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
