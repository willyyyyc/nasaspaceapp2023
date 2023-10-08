from Note import Note


class Sound:
    def __init__(self, notes: list[Note]):
        notes: list[Note] = notes
        self.sound = notes[0].audio
        for note_i in range(1, len(notes)):
            self.sound.overlay(notes[note_i].audio)
    
    def __add__(self, other: 'Sound') -> 'Sound':
        return self.sound + other.sound

    def play(self):
        self.sound.play()
    