import math
from music21 import chord

class MusicAttributes:
    def __init__(self, intensity, size):
        self.intensity = intensity
        self.size = size

def map_attributes_to_music(star):
    # Map intensity to chords
    if star.intensity < 190:
        chords = [chord.Chord(['C4', 'E4', 'G4'])]  # Example chord for low intensity
    elif 190 <= star.intensity < 250:
        chords = [chord.Chord(['D4', 'F4', 'A4'])]  # Example chord for medium intensity
    else:
        chords = [chord.Chord(['E4', 'G4', 'B4'])]  # Example chord for high intensity

    # Map size to volume
    volume = math.log(star.size) * 4  # Example scaling for volume

    return chords, volume

# Example usage:
attributes = MusicAttributes(intensity=0.5, size=0.8)
mapped_chords, mapped_volume = map_attributes_to_music(attributes)

print("Mapped Chords:", mapped_chords)
print("Mapped Volume:", mapped_volume)
