import cv2

cap = cv2.VideoCapture(-1)

i = 1 
while True:
    key = -1
    while key == -1:
        key = cv2.waitKey(1)
        ret, frame = cap.read()
        mirror = cv2.flip(frame, 1)
        cv2.imshow("Camara", mirror)

    if key == 27:
        break
    if key == ord(' '):
        print("Photo taken")
        cv2.imshow("Foto", mirror)
        cv2.imwrite(f'./captures/image_{i}.jpg', mirror)
        i += 1

cap.release()
cv2.destroyAllWindows()