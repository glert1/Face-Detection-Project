import dlib
import cv2


cnn_face_det = dlib.cnn_face_detection_model_v1('dlib/mmod_human_face_detector.dat')

image = cv2.imread('/your image path')
image = cv2.resize(image, (800,600))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = cnn_face_det(gray, 1)

for face in faces:
    rect =  face.rect
    x, y, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()
    cv2.rectangle(image, (x, y), (x2, y2), (0, 0, 255), 2)

    
cv2.imshow('dlib cnn', image)
cv2.waitKey(0)
