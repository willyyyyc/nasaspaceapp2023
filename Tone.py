class Tone:
    def __init__(self, audio):
        self.audio = audio

    def play(self):
        return(f"Playing tone with volume {self.volume} and pitch {self.pitch} Hz")



