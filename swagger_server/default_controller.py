from swagger_server.controllers.load_video import load_video
import connexion
import six

from Song import Song
from Sound import Sound
from Video import Video  
from Frame import Frame
import statistics
from Note import Note
from music21 import chord, stream, volume
from music_lib import create_chords_from_stars
import math
from pydub import AudioSegment
from pydub.playback import play


from swagger_server.models.video_sonograph_body import VideoSonographBody  # noqa: E501
from swagger_server import util


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

def video_sonograph_post(body):  # noqa: E501
    """Represent a video of space with sound

    Takes a video URL and returns an audio file or audio URL. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = VideoSonographBody.from_dict(connexion.request.get_json())  # noqa: E501
    load_video(body.video_url)
    
    video = Video("tmp_vid.mp4")
    
    sounds = []

    chords = []

    # Create a stream for the entire composition
    composition_stream = stream.Stream()

    for i in range(0, len(video.frames), 15):
        frame = video.frames[i]

        stars = get_stars(frame)

        # Create a chord or note sequence for stars in the frame
        frame_chord = chord.Chord([create_chords_from_stars(star) for star in stars])
        
        vel = math.log(statistics.mean([star.size for star in stars]))*10
        
        chord_vol = volume.Volume(velocity=vel)

        frame_chord.volume = chord_vol

        # Append the frame's chord to the composition
        composition_stream.append(frame_chord)
    
    composition_stream.write('midi', 'combined_sound.mid')

    # return the midi file as a byte stream
    with open('combined_sound.mid', 'rb') as file:
        midi_bytes = file.read()
        return midi_bytes
