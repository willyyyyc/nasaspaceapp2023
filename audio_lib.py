from pydub import AudioSegment
from pydub.playback import play
import Star
import math

class Note:
    def __init__(self, audio_file):
        unshortened_audio = AudioSegment.from_file(audio_file)
        shortened_audio = unshortened_audio[0:30]
        self.playable_tone = shortened_audio
        
    
    def play_tone(self):
        play(self.playable_tone)

    def increase_volume(self, xDB):
        self.playable_tone = self.playable_tone + xDB  


octave = {"a": Note("piano-keys/piano_a.wav"), 
          "b": Note("piano-keys/piano_b.wav"), 
          "c": Note("piano-keys/piano_c.wav"), 
          "d": Note("piano-keys/piano_d.wav"),
          "e": Note("piano-keys/piano_e.wav"),
          "f": Note("piano-keys/piano_f.wav"),
          "g": Note("piano-keys/piano_g.wav")}

def play_note(key):
    octave.get(key).play_tone()

def increase_and_play(key, xDB):
    octave.get(key).increase_volume(xDB)

def star_to_music(star):
    size = math.log(star.size) * 4
    intensity = star.intensity
    if (65 <= intensity < 70):
        octave.get("a").increase_volume(size)
        return octave.get("a")
    elif (70 <= intensity < 75):
        octave.get("b").increase_volume(size)
        return octave.get("b")
    elif (75 <= intensity < 80):
        octave.get("c").increase_volume(size)
        return octave.get("c")
    elif (80 <= intensity < 85):
        octave.get("d").increase_volume(size)
        return octave.get("d")
    elif (85 <= intensity < 90):
        octave.get("e").increase_volume(size)
        return octave.get("e")
    elif (90 <= intensity < 95):
        octave.get("f").increase_volume(size)
        return octave.get("f")
    elif (95 <= intensity < 100):
        octave.get("g").increase_volume(size)
        return octave.get("g")
