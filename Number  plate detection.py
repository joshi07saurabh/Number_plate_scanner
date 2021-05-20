import cv2
farmeWidth = 640
frameHeight = 480
npPlateCascade = cv2.CascadeClassifier("resourse/haarcascade_russian_plate_number.xml")
minarea = 200
cap = cv2.VideoCapture(0)
cap.set(3, farmeWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0
while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numbers = npPlateCascade.detectMultiScale(gray, 1.1, 10)
    for (x,y,w,h) in numbers:
        area = w*h
        if area > minarea:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            imgSave = img[y:y+h,x:x+w]
            cv2.imshow("Save",imgSave)
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("resourse/scanned/No_plate_"+str(count)+".jpg",imgSave)
        cv2.rectangle(img,(100,200),(440,250),(255,0,255),cv2.FILLED)
        cv2.putText(img,"Saved",(200,240),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.imshow("image",img)
        cv2.waitKey(500)
        count += 1

