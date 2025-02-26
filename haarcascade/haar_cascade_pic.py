import cv2


img = cv2.imread('/your image path')
img = cv2.resize(img, (800,600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_detector=cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')


faces = face_detector.detectMultiScale(gray, 1.06, 5)

for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)


cv2.imshow('Haar Cascade', img)
cv2.waitKey(0)
cv2.destroyAllWindows()