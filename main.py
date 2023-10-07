from Video import Video  
from Frame import Frame

def get_stars(frame: 'Frame') -> 'Frame':
    """function responsible for optimizing the image to find stars
    and returning the highest quality stars to be converted to tones

    Args:
        frame (Frame): _description_

    Returns:
        Frame: _description_
    """
    # Convert the frame to grayscale
    grayscale_frame = frame.get_grayscale()

    blurred_frame = grayscale_frame.get_blurry()

    # set threshold value
    thresholded_frame = blurred_frame.threshold(127)

    # Find all high-intensity regions
    contours, stars = thresholded_frame.find_high_intensity_regions()

    contours.display(window_name='Contours')
    
    stars_filtered = [star for star in stars if star.size > 5]

    return stars_filtered

if __name__ == "__main__":
   
    video = Video("media/spaceVid.mp4")
    
    for frame in video.frames:
        
        stars = get_stars(frame)

        for star in stars:
            print(star)
        
        break