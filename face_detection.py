import cv2

#Loading the the classifer
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the input image
img = cv2.imread('test.jpg')

#Converting into grayscale mode
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#Displaying the output image
cv2.imshow('img', img)
cv2.waitKey()