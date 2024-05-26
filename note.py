from facenet_pytorch import MTCNN
import cv2

# Initialize MTCNN
mtcnn = MTCNN()
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    
    # Detect faces
    boxes, _ = mtcnn.detect(frame)
    
    if boxes is not None:
        for box in boxes:
            # Unpack the bounding box differently
            x1, y1, x2, y2 = box.astype(int)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
