import cv2

fist = cv2.CascadeClassifier("./haarcascades/fist.xml")
palm = cv2.CascadeClassifier("./haarcascades/palm.xml")
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fists = fist.detectMultiScale(gray, 1.3, 5)
    palms = palm.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in fists:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 45, 45), 2)
        print("fist")
    for x, y, w, h in palms:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 45, 45), 2)
        print("palm")

    cv2.imshow("frame", frame)



    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
