import dlib
import cv2

hog_face_detector = dlib.get_frontal_face_detector()

video = cv2.VideoCapture(0)  

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = hog_face_detector(gray)

    for i, face in enumerate(faces):
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)


    cv2.imshow("Face Detection - HOG", frame)
    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()
