import cv2

face_detector = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)  

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Haar Cascade ', frame)
    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()
