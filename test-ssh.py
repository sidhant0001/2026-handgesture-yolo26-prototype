# Simple test program to see if my code runs on the Raspberry Pi
# If I see "aarch64" in the output, that means it really ran on the Pi!

import cv2
import platform
from datetime import datetime

print("Hello from my Pi test program!")
print("--------------------------------")

# Print some info so I can check where this is running
right_now = datetime.now()
print("Time right now:", right_now)
print("Computer name:", platform.node())
print("Computer type:", platform.machine())   # should say "aarch64" on the Pi
print("OpenCV version:", cv2.__version__)
print("--------------------------------")

# Try to open the webcam (0 means the first camera plugged in)
my_camera = cv2.VideoCapture(0)

if my_camera.isOpened() == True:
    print("Camera is working! Taking a picture...")
    got_picture, picture = my_camera.read()

    if got_picture == True:
        print("Got the picture! Size is:", picture.shape)
        cv2.imwrite("test_picture.jpg", picture)
        print("Saved it as test_picture.jpg")
    else:
        print("Camera opened but I couldn't get a picture :(")

    my_camera.release()   # always close the camera when done
else:
    print("Could not open the camera. Is the webcam plugged in?")