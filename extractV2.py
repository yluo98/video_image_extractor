'''
Purpose: Program uses OpenCV that asks user for start time, end time, and
the time for frame extraction, then extracts the desired frames in
jpeg images from the video.
Run: Enter "python sec_split.py" in terminal and answer the required input
'''
import cv2
import os

# Creates a data file to store images
try:
    if not os.path.exists("../extracted_data"):
        os.makedirs("../extracted_data")
except OSError:
    print('Error: Creating directory of ../extracted_data')

# Ask user to choose a video to capture
video = raw_input("Enter the video name for frame extraction:       ")

# Ask user for when to start
startNum = input("Enter the time (in sec) for when to start:       ")

# Ask user for when to end
endNum = input("Enter the time (in sec) for when to end:         ")
endNum *= 1000

# Ask user for the time when frames are to be extracted
num = input("Enter the time (in sec) for frame extraction:    ")

# Playing video from file:
vidcap = cv2.VideoCapture("../videos/" + video)
success, image = vidcap.read()

sec = startNum  # seconds of the video to be labeled
frame = num * 1000  # frame to be added
currentFrame = (startNum * 1000)  # keeps track of frame

while(currentFrame <= endNum):
    # Sets video time
    vidcap.set(cv2.CAP_PROP_POS_MSEC, currentFrame)

    # Capture frame-by-frame
    success, image = vidcap.read()

    # Generates and saves image
    if(success):
        # Saves image of the current frame in jpg file
        name = "../extracted_data/frame_" + str(sec) + "s.jpg"
        print("Creating..." + name)
        cv2.imwrite(name, image)

    # To stop duplicate images
    sec += num
    currentFrame += frame

# Stop everything
print("extractedV2.py Executed!")
vidcap.release()
cv2.destroyAllWindows()
