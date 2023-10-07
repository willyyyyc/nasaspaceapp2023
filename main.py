from Video import Video  

if __name__ == "__main__":
   
    video = Video("media/spaceVid.mp4")
    
    for frame in video.frames:
        # Convert the frame to grayscale
        grayscale_frame = frame.get_grayscale()

        # Find all regions of intensity
        thresholded_frame = grayscale_frame.threshold(127)

        frame.display()