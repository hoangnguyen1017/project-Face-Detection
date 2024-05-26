from tkinter import *
import cv2
import os
from database import *
import database
from tkinter import messagebox
from CNN_train import *
from Recognition_CNN_train import*
from pass_encrypt import *
from facenet_pytorch import MTCNN
# from Training import *
#from Recognition import *

def register_window():
    r = Toplevel()
    r.geometry("500x600")
    r.title("Face Recognition")
    r.resizable(False, False)

    show_icon = PhotoImage(file='show_icon.png')
    hide_icon = PhotoImage(file='hide_icon.png')
    show_icon= show_icon.subsample(7)
    hide_icon= hide_icon.subsample(7)
    class WebcamApp:
        def start_capture(self, r):
            cam = cv2.VideoCapture(0)
            mtcnn = MTCNN()
            if not cam.isOpened():
                print("Error: Could not open webcam.")
                exit()

            cam.set(3, 640)
            cam.set(4, 480)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            if face_cascade.empty():
                messagebox.showerror(title="Error",message="Failed to load face cascade classifier")
                print("Error: Failed to load face cascade classifier.")
                exit()

            def show_passwordConfirm():
                if  passConfirm_entry['show']== '' :
                    passConfirm_entry.config(show='*')
                    show_hide_bttn2.config(image=hide_icon)
                else:         
                    passConfirm_entry.config(show='')
                    show_hide_bttn2.config(image=show_icon)

            def show_pass():
                if pass_entry['show']== '':
                    pass_entry.config(show='*')
                    show_hide_bttn1.config(image=hide_icon)
                else:
                    pass_entry.config(show='')
                    show_hide_bttn1.config(image=show_icon)

            #Label
            lb_titel = Label(r, text="Register", fg="red", font="arial 30")
            lb_titel.place(x=170, y=80)

            input_name = StringVar()
            lb_name = Label(r, text="Username: ", font="arial 10")
            lb_name.place(x=50, y=200)

            input_pass = StringVar()
            lb_pass = Label(r, text="Password: ", font="arial 10")
            lb_pass.place(x=50, y=240)

            lb_guid_passw1 = Label(r, text="Must be Okay strength or better")
            lb_guid_passw1.place(x=130, y=280)
            lb_guid_passw2 = Label(r, text="Password is at least 11 characters long.")
            lb_guid_passw2.place(x=130, y=300)

            input_passConfirm = StringVar()
            lb_confirmPass = Label(r, text="Confirm Password: ", font="arial 10")
            lb_confirmPass.place(x=50, y=330)

            #Entry
            name_entry = Entry(r, bg="white", width="35", fg="black", font="arial 10", textvariable=input_name)
            name_entry.place(x=130, y=200)

            pass_entry = Entry(r, bg="white",  width="35", fg="black", font="arial 10",show="*", textvariable=input_pass)
            pass_entry.place(x=130, y=240)

            passConfirm_entry = Entry(r, bg="white", width="35", fg="black", font="arial 10",show='*', textvariable=input_passConfirm)
            passConfirm_entry.place(x=130, y=355)

            show_hide_bttn1 = Button(r, image=hide_icon,bd=0,command=show_pass)
            show_hide_bttn1.place(x=380,y=237)

            show_hide_bttn2 = Button(r, image=hide_icon,bd=0,command=show_passwordConfirm)
            show_hide_bttn2.place(x=380,y=352)
            

            def isNameValid(input_var):
                input_str = input_var.get()
                if input_str.replace(" ", "").isalpha():
                    return True
                else:
                    lb_error_name = Label(r, text="The Name format must be a character", fg="red", font="arial 8")
                    lb_error_name.place(x=130, y=270)
                    return False

            def isPassValid(input_var):
                input_str = input_var.get()
                if len(input_str) >= 11:
                    return True
                else:
                    lb_error_passw = Label(r, text="Password must be at least 11 characters long", fg="red", font="arial 8")
                    lb_error_passw.place(x=130, y=260)
                    return False

            def quit():
                r.destroy()

            def capture():    
                if isNameValid(input_name) and (isPassValid(input_pass) == isPassValid(input_passConfirm)):
                    directory = 'dataset'
                    existing_folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
                    folder_id = len(existing_folders) + 1
                    name_str = input_name.get()
                    passw_str = input_pass.get()
                    passw_Conf_str = input_passConfirm.get()  
                    
                    #hash password
                    passwords = []               
                    hashed_password_salt= hash_password_salt(passw_str)
                    passwords.append((hashed_password_salt))
                    if passw_str == passw_Conf_str:
                        database.addUser(folder_id,name_str,passwords[0])
                        database.admin()
                    else:
                        lb_passConf = Label(r, text="Your password is incorrect!", fg="red")     
                        lb_passConf.place(x=130, y=374)      
                        return
                else:
                    lb_error.config(text=database.c)
                    return

                if not os.path.exists(directory):
                    os.makedirs(directory)
                name_folder_with_id = f"{folder_id}_{name_str}"

                name_folder = os.path.join(directory, name_folder_with_id)

                if not os.path.exists(name_folder):
                    os.makedirs(name_folder)
                else:
                    print("Folder already exists!")
                count = 0
                
                while True:
                    ret, img = cam.read()
                    if not ret:
                        b = messagebox.showerror(title="Error",message="Failed to capture image")
                        lb_error.config(text=b)
                        messagebox.showerror(title="Error",message="Failed to capture image")
                        print("Error: Failed to capture image.")
                        break

                    boxes, _ = mtcnn.detect(img)            
                    if boxes is not None:
                        for box in boxes:
                            x1, y1, x2, y2 = box.astype(int)
                            x1 -= 30  
                            y1 -= 30  
                            x2 += 30  
                            y2 += 30  
                            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                            face_img = img[y1:y2, x1:x2]
                            resized_face = cv2.resize(face_img, (128, 128))
                            count += 1
                            file_path = f"{name_folder}/pic_{name_folder_with_id}_{passwords[0]}_{count}.jpg"
                            cv2.imwrite(file_path, resized_face)

                        cv2.imshow('image', img)

                    k = cv2.waitKey(1) & 0xff
                    if k == 27:
                        break
                    elif count >= 50:
                        break
                lb_AccSucc = Label(r, text="Account succesfull created", fg="red")     
                lb_AccSucc.place(x=130, y=372)          
                lb_comp = Label(r, text="Image capture complete!", fg="red", font="arial 15")
                lb_comp.place(x=150, y=500)
                cam.release()
                cv2.destroyAllWindows()

            lb_error = Label(r,text="")
            lb_error.pack()

            def training():
                try:
                    training_data()
                    lb_train = Label(r,text='Training completed successfully',fg= 'red',font='arial 10',)  
                    lb_train.place(x=240, y=430)  
                except:
                    messagebox.showerror(title="Error",message="Training failed")
            def recognition_recomd():
                recognition()
            bttn_capture = Button(r, text="Start Capture", command=capture)
            bttn_capture.place(x=140, y=400)

            bttn_Train = Button(r, text="Training data", command=training)
            bttn_Train.place(x=140, y=430)

            bttn_Recognition = Button(r, text="Recognition", command=recognition_recomd)
            bttn_Recognition.place(x=140, y=460)

            bttn_quit = Button(r, text="Quit", command=quit)
            bttn_quit.place(x=240, y=400)

    app = WebcamApp()
    app.start_capture(r)
    r.mainloop()

#register_window()
