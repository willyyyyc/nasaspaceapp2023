class Song:
    def __init__(self, sounds):
        self.sounds = sounds
        self.song = sounds[0].sound
        
        for sound in sounds[1:]:
            self.song + sound.sound
