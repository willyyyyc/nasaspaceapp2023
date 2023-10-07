from pydub import AudioSegment
from pydub.playback import play
import Star
import math

class Note:
    def __init__(self, audio_file):
        self.playable_tone = AudioSegment.from_file(audio_file)
    
    def play_tone(self):
        play(self.playable_tone)

    def increase_volume(self, xDB):
        play(self.playable_tone + xDB)

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
        increase_and_play("a", size)
    elif (70 <= intensity < 75):
        increase_and_play("b", size)
    elif (75 <= intensity < 80):
        increase_and_play("c", size)
    elif (80 <= intensity < 85):
        increase_and_play("d", size)
    elif (85 <= intensity < 90):
        increase_and_play("e", size)
    elif (90 <= intensity < 95):
        increase_and_play("f", size)
    elif (95 <= intensity < 100):
        increase_and_play("g", size)

