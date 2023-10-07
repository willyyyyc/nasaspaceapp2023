from Tone import Tone


class Sound:
    def __init__(self, tones: list[Tone]):
        tones: list[Tone] = tones
        self.sound = tones[0].audio
        for tone_i in range(1, len(tones)):
            self.sound.overlay(tones[tone_i].audio)
    
    def __add__(self, other: 'Sound') -> 'Sound':
        return self.sound + other.sound

    def play(self):
        self.sound.play()
    