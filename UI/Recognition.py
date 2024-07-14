
import sqlite3
import cv2
from database import fetch_one

def recognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Train/trainingData.yml')

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    conn = sqlite3.connect('Face_db.db')

    def getProfile(id):
        query = "SELECT * FROM User WHERE id =" + str(id)
        cursor = conn.execute(query)
        profile = None
        for row in cursor:
            profile =row
        return profile

    cap = cv2.VideoCapture(0)

    fontface = cv2.FONT_HERSHEY_COMPLEX
    while True:
        ret, frame = cap.read()
        
        if not ret:  
            print("Error: Couldn't read frame from the video capture device")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y: y+h, x: x+w]

            id, confidence = recognizer.predict(roi_gray)
    
            if confidence < 80:
                profile = getProfile(id)
                if profile is not None:
                    cv2.putText(frame, f"{str(profile[1])} ({int(100 - confidence)}% confidence)", (x+10, y+h+30), fontface, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x+10, y+h+30), fontface, 1, (0, 255, 0), 2)

        cv2.imshow('Image', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


