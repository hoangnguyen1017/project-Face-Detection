import cv2
import numpy as np
import os
from keras import  models
from facenet_pytorch import MTCNN
def recognition():
    model = models.load_model('model_face_10epochs.keras')

    cam = cv2.VideoCapture(0)
    mtcnn = MTCNN()
    data = 'dataset'
    names = []
    ids = []
    for folder in os.listdir(data):
        folder_path = os.path.join(data, folder)
        if os.path.isdir(folder_path): 
            filename = folder.split('_')[1]
            id = folder.split('_')[0]
            names.append(filename)
            ids.append(id)
    if not names and not ids:
        print("No names found in the dataset directory.")

    while True:
        ret, frame = cam.read()
        
        boxes, _ = mtcnn.detect(frame)
        if boxes is not None:
            for box in boxes:
                x1, y1, x2, y2 = box.astype(int)
                x1 -= 30  
                y1 -= 30  
                x2 += 30  
                y2 += 30  

                roi = cv2.resize(frame[max(0, y1):min(frame.shape[0], y2), max(0, x1):min(frame.shape[1], x2)], (128, 128))
                result = np.argmax(model.predict(roi.reshape((-1, 128, 128, 3))))

                for id, name in zip(ids, names):
                    if str(result) == id:
                        cv2.putText(frame, str(name), (x1+15, y1-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
#recognition()

    