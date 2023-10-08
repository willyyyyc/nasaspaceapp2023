import math
from music21 import stream, instrument, chord, volume

def combine_chords_into_music(chords):
    # Create a stream for the entire composition
    composition_stream = stream.Stream()
    composition_stream.append(instrument.Piano())  # You can choose any instrument

    # Create a melody using the mapped chords
    melody_stream = stream.Part()
    melody_stream.append(instrument.Piano())  # You can choose any instrument

    for chord_obj in chords:
        melody_stream.append(chord_obj)

    # Add the melody to the composition
    composition_stream.append(melody_stream)

    return composition_stream

def create_chords_from_stars(star):
    # Map star attributes to a single chord
    if star.intensity is not None and star.size is not None:
        # Map intensity to chords
        if star.intensity < 200:
            chord_symbol = 'C4'  # Example chord for low intensity
        elif 200 <= star.intensity < 220:
            chord_symbol = 'D4'  # Example chord for medium intensity
        else:
            chord_symbol = 'E4'  # Example chord for high intensity

        # Create the chord
        chord_obj = chord.Chord([chord_symbol])

        return chord_obj
    return None