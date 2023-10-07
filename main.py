from Video import Video  

if __name__ == "__main__":
   
    video = Video("media/spaceVid.mp4")
    
    for frame in video.frames:
        # Convert the frame to grayscale
        grayscale_frame = frame.get_grayscale()

        blurred_frame = grayscale_frame.get_blurry()

        # set threshold value
        thresholded_frame = blurred_frame.threshold(127)

        # Find all high-intensity regions
        contours, stars = thresholded_frame.find_high_intensity_regions()

        contours.display(window_name='Contours')
        
        stars_filtered = [star for star in stars if star.size > 5]

        for star in stars_filtered:
            pass
        
        break