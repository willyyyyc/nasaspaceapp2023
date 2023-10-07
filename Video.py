import cv2 as cv
from Frame import Frame  


class Video:
    """class to manage loading and modifying video files"""
    def __init__(self, title):
        self.filename = title
        self.cap = cv.VideoCapture(self.filename)
        self.cap.open(self.filename)
        self.frames: list[Frame] = []
        self.load_frames()

    def load_frames(self):
        """loads images from video"""
        frames = []
            
        # Check if the video file was opened successfully
        if not self.cap.isOpened():
            print("Error: Could not open video.")
            return frames
        
        while True:
            # Read the next frame from the video
            ret, frame = self.cap.read()

            # If the video has ended, break out of the loop
            if not ret:
                break
            
            frame_obj = Frame(frame)

            # Append the frame to the list
            frames.append(frame_obj)

        self.frames = frames

    def __str__(self):
        return self.filename
    