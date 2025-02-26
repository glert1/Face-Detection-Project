import dlib
import cv2

cnn_face_detector = dlib.cnn_face_detection_model_v1('dlib/mmod_human_face_detector.dat')

video = cv2.VideoCapture(0)  


while True:
    ret, frame = video.read()
    if not ret:
        break

    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = cnn_face_detector(gray_frame, 1)  

   
    for face in faces:
        rect = face.rect  
        x, y, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()
        cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
    

    cv2.imshow("CNN Face Detection", frame)
    cv2.waitKey(1)

    
video.release()
cv2.destroyAllWindows()
