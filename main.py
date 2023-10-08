from Song import Song
from Sound import Sound
from Video import Video  
from Frame import Frame
from Note import Note
from audio_lib import octave
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
    
    stars_filtered = [star for star in stars if star.size > 5]

    return stars_filtered

def star_to_music(star):
    size = math.log(star.size) * 4
    intensity = star.intensity
    if (127 <= intensity < 146):
        audio_file = octave.get("a")
        new_note_a = Note(audio_file, size)
        return new_note_a
    elif (146 <= intensity < 165):
        audio_file = octave.get("b")
        new_note_b = Note(audio_file, size)
        return new_note_b
    elif (165 <= intensity < 184):
        audio_file = octave.get("c")
        new_note_c = Note(audio_file, size)
        return new_note_c    
    elif (184 <= intensity < 203):
        audio_file = octave.get("d")
        new_note_d = Note(audio_file, size)
        return new_note_d
    elif (203 <= intensity < 222):
        audio_file = octave.get("e")
        new_note_e = Note(audio_file, size)
        return new_note_e
    elif (222 <= intensity < 241):
        audio_file = octave.get("f")
        new_note_f = Note(audio_file, size)
        return new_note_f
    elif (241 <= intensity < 256):
        audio_file = octave.get("g")
        new_note_g = Note(audio_file, size)
        return new_note_g

if __name__ == "__main__":
   
    video = Video("media/spaceVid.mp4")
    
    sounds = []

    for frame in video.frames:
        
        stars = get_stars(frame)

        notes = []

        for star in stars:
            notes.append(star_to_music(star))
            print(star)
        
        sound = Sound(notes)

        sounds.append(sound)
    
    song = Song(sounds)

    
