'''
Find | Detect | Classification Hands | On Video

About "Input variables":
[cap] - Path to you video file
[LEFT_HAND_COLOR] - Color in RGB format, which will display the left hand
[RIGHT_HAND_COLOR] - Color in RGB format, which will display the right hand
[BORDER_SIZE] - Border size
[SCALE_IMAGE] - Zoom in on the image

"What did I use?"
 * To find the hands on the image - OpenCV HaarCascade (.xml),
   which was fully trained by me.
 * To For recognition of the left and right hand - a simple binary classifier
   that works with convolutional neural networks. To create the model, the
   Keras library was used, and on the backend - TensorFlow.
   
Comments:
 - Since I didn't have much time and computing resources, the
   model of detection and classification is not terrific. But I think that
   for two weeks it's a not bad result :)

Author: Nazar Ponochevnyi
'''

import os
import cv2
import imghdr
import numpy as np
from keras.models import model_from_json


# Input variables
cap = cv2.VideoCapture(0) # Import your video
LEFT_HAND_COLOR = (255, 0, 0) # red color
RIGHT_HAND_COLOR = (0, 0, 255) # blue color
BORDER_SIZE = 1 # 1 - 1px | 2 - 2px
SCALE_IMAGE = 1 # 1 - don't scaling | 2 - scaling two times


# Import cascade and model
hand_cascade = cv2.CascadeClassifier('./weights/DetectionHand.xml')
left_right_model_file = open('./weights/ClassificationHand_model.json', 'r')
left_right_model = model_from_json(left_right_model_file.read())
left_right_model.load_weights('./weights/ClassificationHand_weights.h5')
left_right_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
left_right_model_file.close()

# Check every frame
while 1:
    # Create frame
    ret, img = cap.read()
    
    # Make gray and detect hands
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    if len(hands) > 2:
        hands = [(x,y,w,h) for (x,y,w,h) in hands if w*h > 836 and w*h < 2801]
    
    # Check every hand
    for (x, y, w, h) in hands:
        # Cut a hand from the image
        roi_color = img[y:y + h, x:x + w]
        
        # Transform the image into a numpy array
        roi_array = np.array(cv2.resize(roi_color, (50, 50)))
        roi_array = roi_array.reshape((1, 50, 50, 3))
        
        # Classify left or right hand and create border of corresponding color
        prediction = round(float(left_right_model.predict(roi_array)))
        cv2.rectangle(img, (x - 1, y + 1), (x + w, y + h - 2), \
                      LEFT_HAND_COLOR if prediction else RIGHT_HAND_COLOR, BORDER_SIZE)
    
    # Show result image with scaling and wait for the key to be pressed
    new_height, new_width = [round(data * SCALE_IMAGE) for data in img.shape[:2]]
    cv2.imshow('video', cv2.resize(img, (new_width, new_height)))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()