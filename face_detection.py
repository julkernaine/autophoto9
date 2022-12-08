def face_det():
    import cv2
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    

#Loading the the classifer
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the input image
    img = cv2.imread('picture.jpg')

#Converting into grayscale mode
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#Displaying the output image

    imS = cv2.resize(img, (960, 540))
    cv2.imshow("output", imS)
    cv2.waitKey()
face_det()
