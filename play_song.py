import pygame

def play_midi(midi_filename):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()


midi_filename = "combined_sound.mid"  # Replace with your MIDI file's filename
play_midi(midi_filename)

# Keep the script running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)