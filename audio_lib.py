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


octave = {"a": "piano-keys/piano_a.wav", 
          "b": "piano-keys/piano_b.wav", 
          "c": "piano-keys/piano_c.wav", 
          "d": "piano-keys/piano_d.wav",
          "e": "piano-keys/piano_e.wav",
          "f": "piano-keys/piano_f.wav",
          "g": "piano-keys/piano_g.wav"}

def play_note(key):
    octave.get(key).play_tone()

def increase_and_play(key, xDB):
    octave.get(key).increase_volume(xDB)

def star_to_music(star):
    size = math.log(star.size) * 4
    intensity = star.intensity
    if (65 <= intensity < 70):
        return AudioSegment.from_file(octave.get("a"))[:33]+size
    elif (70 <= intensity < 75):
        return AudioSegment.from_file(octave.get("b"))[:33]+size
    elif (75 <= intensity < 80):
        return AudioSegment.from_file(octave.get("c"))[:33]+size
    elif (80 <= intensity < 85):
        return AudioSegment.from_file(octave.get("d"))[:33]+size
    elif (85 <= intensity < 90):
        return AudioSegment.from_file(octave.get("e"))[:33]+size
    elif (90 <= intensity < 95):
        return AudioSegment.from_file(octave.get("f"))[:33]+size
    elif (95 <= intensity < 100):
        return AudioSegment.from_file(octave.get("g"))[:33]+size