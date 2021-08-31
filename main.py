# idk what im doing
import cv2
import sys

print("""
  ______         _       _   _____                            _ _   _             
 |  ____|       (_)     | | |  __ \                          (_) | (_)            
 | |__ __ _  ___ _  __ _| | | |__) |___  ___ ___   __ _ _ __  _| |_ _  ___  _ __  
 |  __/ _` |/ __| |/ _` | | |  _  // _ \/ __/ _ \ / _` | '_ \| | __| |/ _ \| '_ \ 
 | | | (_| | (__| | (_| | | | | \ \  __/ (_| (_) | (_| | | | | | |_| | (_) | | | |
 |_|  \__,_|\___|_|\__,_|_| |_|  \_\___|\___\___/ \__, |_| |_|_|\__|_|\___/|_| |_|
                                                   __/ |                          
                                                  |___/                           
BY ADAM SARHAN
""")

print('[*] Starting\n[!]Press Q to quit')


def recognize(image):
    imagePath = image
    cascPath = sys.argv[1]

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Faces found', image)


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    cv2.imwrite('frame.jpg', frame)
    recognize('frame.jpg')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
