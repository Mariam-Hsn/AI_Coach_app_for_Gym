from collections import deque
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os


# load saved model from PC
LRCN_model = tf.keras.models.load_model(r'LRCN_model___Date_Time_2024_05_16__18_06_16___Loss_0.005097426939755678___Accuracy_1.0.h5')
LRCN_model.summary()
data_dir = 'dataset'
#getting the labels form data directory
labels = os.listdir(data_dir)

print(labels)
SEQUENCE_LENGTH = 20
IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64


# Initialize the VideoCapture object to read from the webcam.

    
    # Get the width and height of the video.

    # Initialize the VideoWriter Object to store the output video in the disk.

    # Declare a queue to store video frames.
frames_queue = deque(maxlen=SEQUENCE_LENGTH)
predicted_class_name = ''

video_reader = cv2.VideoCapture(0)  # Use webcam device index 0
    # Iterate until the video is accessed successfully.
while (True):

        # Read the frame.
    _, frame = video_reader.read()

        # Check if frame is not read properly then break the loop.
    #if not ok:
        #break
        # Resize the Frame to fixed Dimensions.
    resized_frame = cv2.resize(frame, (64,64))

        # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1.
    normalized_frame = resized_frame / 255

        # Appending the pre-processed frame into the frames list.
    frames_queue.append(normalized_frame)

        # Check if the number of frames in the queue are equal to the fixed sequence length.
    if len(frames_queue) == SEQUENCE_LENGTH:

            # Pass the normalized frames to the model and get the predicted probabilities.
            predicted_labels_probabilities = LRCN_model.predict(np.expand_dims(frames_queue, axis=0))[0]

            # Get the index of class with highest probability.
            predicted_label = np.argmax(predicted_labels_probabilities)

            # Get the class name using the retrieved index.
            predicted_class_name = labels[predicted_label]

        # Write predicted class name on top of the frame.
    cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        # Display the frame
    cv2.imshow('Live Video', frame)

        # Break the loop if 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    # Release the VideoCapture and VideoWriter objects.
video_reader.release()
cv2.destroyAllWindows()