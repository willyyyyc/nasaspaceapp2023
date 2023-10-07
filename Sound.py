class Sound:
    def __init__(self, tone):
        self.tone: int = tone

    def play(self):
        self.tone.play()
        
    