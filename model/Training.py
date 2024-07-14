
import cv2
import numpy as np
from PIL import Image as PILImage 
import os
from tkinter import *
def training_data ():
    def getImageWithID(data):
        faces = []
        IDs = []

        for folder in os.listdir(data):
            folder_path = os.path.join(data, folder)
            if os.path.isdir(folder_path):
                imagePaths = [os.path.join(folder_path, i) for i in os.listdir(folder_path)]
                
                for imagePath in imagePaths:
                    faceImg = PILImage.open(imagePath).convert('L')
                    faceNp = np.array(faceImg,'uint8')
                    ID = int(folder.split('_')[0])  
                    
                    faces.append(faceNp)
                    IDs.append(ID)
                    print(faces)
                    print(IDs)
                    cv2.imshow('Training', faceNp)
                    cv2.waitKey(100)  
        cv2.destroyAllWindows()
        return faces, IDs

    data = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces, IDs = getImageWithID(data)

    try:
        recognizer.train(faces, np.array(IDs))
        recognizer.save('Train/trainingData.yml')
        
        
        print("Success: Training completed successfully.")
    except :
        print("Error:")

    if not os.path.exists('Train'):
        os.makedirs('Train')


