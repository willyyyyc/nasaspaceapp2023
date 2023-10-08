from pydub import AudioSegment
from pydub.playback import play

class Note:
    def __init__(self, audio_file):
        unshortened_audio = AudioSegment.from_file(audio_file)
        shortened_audio = unshortened_audio[0:30]
        self.playable_tone = shortened_audio
        
    
    def play_tone(self):
        play(self.playable_tone)

    def increase_volume(self, xDB):
        self.playable_tone = self.playable_tone + xDB  