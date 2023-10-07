class Tone:
    def __init__(self, volume=0.5, pitch=440):
        self.volume: int = volume
        self.pitch:int = pitch

    def play(self):
        return(f"Playing tone with volume {self.volume} and pitch {self.pitch} Hz")



