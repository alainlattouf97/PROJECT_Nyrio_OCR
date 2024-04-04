
from pyniryo2 import *
import pyniryo
import cv2
from PIL import Image, ImageOps
import numpy as np
from pytesseract import * 
 
from OCR import *


 
### It is a bit paricual here , you need to use a combination between Pyniryo and Pyniryo2. 
### So the get_img_compressed and get_camera_intrinsics need to be with pyniryo2
### and uncompress_image and undistort_image need to use pyniryo.








cap= cv2.VideoCapture(0)

# Check if the webcam was opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    

# Read and display each frame from the webcam
while True:
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break


    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    test_image = preprocess_image(gray_frame,size)
    prediction = model.predict(test_image)
    predicted_class_index = np.argmax(prediction)
    predicted_class = label_binarizer.classes_[predicted_class_index]

    print("Prédiction du caractère:", predicted_class)

    
    # Display the frame
    cv2.imshow('Webcam', gray_frame)

    # Check for key press; if 'q' is pressed, exit the loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the webcam capture object and close the window
cap.release()
cv2.destroyAllWindows()