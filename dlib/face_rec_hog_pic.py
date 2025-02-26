import dlib
import cv2

image = cv2.imread('/your image path')
image = cv2.resize(image, (600,600))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hogFaceDetector = dlib.get_frontal_face_detector()
faces = hogFaceDetector(gray, 1)

for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)

cv2.imshow('dlib hog', image)
cv2.waitKey(0)
