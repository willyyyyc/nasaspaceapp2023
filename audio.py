from pydub import AudioSegment
from pydub.playback import play

class Note:
    def __init__(self, audio_file):
        self.playable_tone = AudioSegment.from_file(audio_file)
    
    def play_tone(self):
        play(self.playable_tone)

    def increase_volume(self, xDB):
        play(self.playable_tone + xDB)

octave = [Note("piano-keys/piano_a.wav"), 
          Note("piano-keys/piano_b.wav"), 
          Note("piano-keys/piano_c.wav"), 
          Note("piano-keys/piano_d.wav"),
          Note("piano-keys/piano_e.wav"),
          Note("piano-keys/piano_f.wav"),
          Note("piano-keys/piano_g.wav")]

def play_note(key):
    piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
    key_to_play = piano_keys.index(key)
    octave[key_to_play].play_tone()

def increase_and_play(key, xDB):
    piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
    key_to_play = piano_keys.index(key)
    octave[key_to_play].increase_volume(xDB)
