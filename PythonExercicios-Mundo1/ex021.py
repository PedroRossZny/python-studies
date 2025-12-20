import pygame
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\pedeo\\Downloads\\Audiomp3.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)