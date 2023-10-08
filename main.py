from Song import Song
from Sound import Sound
from Video import Video  
from Frame import Frame
from Note import Note
from music21 import chord, stream
from music_lib import create_chords_from_stars, combine_chords_into_music
import math
from pydub import AudioSegment
from pydub.playback import play

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
    _, stars = thresholded_frame.find_high_intensity_regions()

    #contours.display(window_name='Contours')
    
    stars_filtered = sorted([star for star in stars if star.size > 5], key=lambda star: star.size, reverse=True)[:3]

    return stars_filtered

if __name__ == "__main__":
   
    video = Video("media/spaceVid.mp4")
    
    sounds = []

    chords = []

    # Create a stream for the entire composition
    composition_stream = stream.Stream()

    for i in range(0, len(video.frames), 15):
        frame = video.frames[i]

        stars = get_stars(frame)

        # Create a chord or note sequence for stars in the frame
        frame_chord = chord.Chord([create_chords_from_stars(star) for star in stars])
        
        # Append the frame's chord to the composition
        composition_stream.append(frame_chord)
    
    composition_stream.write('midi', 'combined_sound.mid')
    
