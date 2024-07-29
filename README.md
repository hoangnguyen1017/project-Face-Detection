# Facial Recognition Application
------
## Table of Content
- Introduction
- Features
- Installation
- Usage
- Set up Project
## Introduction
Welcome to the Face Recognition Project! This project leverages the powerful *FaceNet model and MTCNN* for face detection, along with a *CNN model* for face recognition through your webcam. *OpenCV* is used to access and display the webcam feed, while FaceNet and MTCNN ensure accurate and efficient face detection. The CNN model provides robust face recognition capabilities, all within a user-friendly graphical *User Interface (UI)*.
## Feature
#### Face Detection
- **Detect Faces**: Capable of detecting faces in images and real-time video streams.
- **Real-Time Detection**: Provides immediate face detection using your webcam.
#### User Interface (UI)
- **Intuitive design**: Clear and user-friendly user interface to get started and manage facial recognition easily.
- **Live Response**: Shows a real-time webcam feed with detected faces highlighted.
##  Installation
|Package|Vesion|
|-------|------|
|Python|3.11|
|Pillow|9.5|
|Numpy|1.24.4|
|facenet_pytorch|2.6.0|
|ultralytics|8.2.22|
|Opencv|4.9.0.80|
|cmake|3.28.3|
|scikit-learn|24.1.1|

## Approach

**Database** : Interact with DB Browser.
- Database connection:

    ```c 
    conn = sqlite3.connect('table_name.db')
    c = conn.cursor()
    ```

- Structured Query Language statements:
    - Select
    - Insert
    - Delete
    - Update
    - From
    - Join
- Support function to execute SQL statements:
    ```c
    def execute_sql(sql, params=()):
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur
    
    def fetch_all(sql):
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    def fetch_one(sql, params=()):
        cur = conn.cursor()
        cur.execute(sql, params)
        return cur.fetchone()
    ```
**Model** : There are 2 ways to train a face recognition model:
1. Local Binary Patterns Histograms (LBPH) algorithm in Python with OpenCV.
2. Deep learning method with convolutional neural network (CNN) for face recognition.

    - **Data Cleaning**
        - After the image is captured from the camera, the image has been resized to 128 × 128 to ensure the size of the images is similar.

    - **Data Preprocessing**
        - The images are then added to the Xtrain (image) and ytrain (label) lists.
        - Next, convert the Xtrain and ytrain lists to NumPy arrays to process the data more quickly and efficiently.
        - Then, the dataset is divided into two parts, 90% of the dataset is used for training and the remaining 10% is used for testing.
    
    - **Component of the CNN network**
        - **Conv2D layers**: These layers learn features from images by applying convolutional filters over data patches.

        - **MaxPooling2D**: This layer reduces the size of the data by selecting the maximum value from non-overlapping regions.

        - **Flatten**: This layer converts data from a matrix format into a vector format, preparing it for Dense layers.

        - **Dense layers**: These fully connected layers connect neurons together to produce the final predictions.

        - **Activation function**: In this case, softmax is often used in the output layer to compute the probabilities of the output classes. the probabilities of the output classes
    - **How to modify parameters in the model**
        - You can add or remove *Conv2D and MaxPooling2D* layers to change the depth of the model
        - Change the number and size of *filters* to tune the model's learning ability.
        - Adjust the *dropout* rate to control the level of regularization and avoid overfitting
        - Change the number of neurons in *Dense layers* to adjust model complexity
        - Change *the activation function* to test the effectiveness of different functions.
        - Adjust the number of *epochs*, *batch size* and *learning rate* to optimize the training process
        - Change the *padding style* to control the output size of Conv2D layers.
    - **Model Summary**
        ![window](cnn.png)

**UI (User Interface)** : How to design and use tkinter application
- How to design
    - Main Window
         ```c
        from tkinter import *
        root = Tk()
        root.geometry("500x600")  
        root.title("Face Recognition")  
        root.resizable(False, False)  kích thước cửa sổ
        root.mainloop()  
        ```
    - Basic Interface Elements
        - **Label**: Used to display text or images.
        - **Button**: Used to execute commands when the user presses.
        - **Entry**: Input field.
        - **Text**: Multi-line input field.
        - **Canvas**: Used to draw images or place other widgets.
        - **Frame**: Frame containing other widgets.
        - **Listbox**: List of selected items.
    - Positioning Components : **pack()**, **grid()**, **place()**

**How to use UI application**   
 
1. **Window**
+ Log in to account (Check if the account and password match the registered account)
![window](window.png)

2. **Register** :
+ Register personal information (name, password)
+ Click the **Start Capture** button to take a photo of your face and save it to your device and list on DB Bowser
![Register](register.png)
+ Click the **training data** button to train data using CNN model or LBPH algorithm based on captured images

+ Convolutional Neural Network Summary
    ![train](train_data.png)
+ Performance Metrics
        + Accuracy: 98%
        + False Positive Rate: 2%

**Recognition, Recognition_CNN**
+ Real-time face recognition based on the above model using CNN model or LBPH algorithm

**Win-manage, Win-Role** (*Incomplete*)

**Admin** : 
+ User Management : Account Creation and Delete, View Information, Permission Management.
+ Content Management : Data Backup and Recovery.
+ User Support and Management : User Interface and Experience Managemen

**Manager** :
+ User Management : Account Creation and Delete, Permission Management.(*unaccomplished*)

**User**
+ View information board

## How to set up Project

- After downloading the folders, move all the files into the same folder to start running
- Database : 
    - Dowload DB Browser (SQLite) 3.12.2
    - Create new database to connect:
    ```c
    from tkinter import messagebox
    import sqlite3

    conn =sqlite3.connect('name_database.db')
    c = conn.cursor()
    ```
    - You can create the Admin role after first registering with the User role and then making changes in the local Admin folder