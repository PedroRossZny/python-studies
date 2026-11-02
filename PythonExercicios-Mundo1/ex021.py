import os
import pygame
pygame.mixer.init()
# Plays Audiomp3.mp3 from this folder; the file is not in the repository.
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'Audiomp3.mp3'))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)