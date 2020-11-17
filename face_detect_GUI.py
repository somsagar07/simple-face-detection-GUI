from tkinter import *
import cv2
import face_recognition

from tkinter.filedialog import askopenfile 
import os
def onOpen():
        file = askopenfile()
        global image1
        y= file.name
        image1= os.path.basename (y)
        file.close()
master = Tk()

def reco():
    image = face_recognition.load_image_file(image1)
    face_locations = face_recognition.face_locations(image)
    for (top, right, bottom, left) in (face_locations):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 3)
    image2=image[:, :, ::-1]
    output = cv2.resize(image2, (560, 600)) 
    cv2.imshow('Output', output)
    cv2.waitKey(1)

master.title("Image Loader") 
master.geometry("500x300") 

master.resizable(width = True, height = True) 
b = Button(master, text="image", command=onOpen)
c = Button(master, text="Output", command=reco)

b.pack()
c.pack()

master.mainloop()