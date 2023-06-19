import os
import pygame
import pip
try:
    from PIL import Image
except:
    pip.main(['install','pillow'])

background_save_path='Cache/image/background_current.png'
darken_factor=0.5
def dim_screen(screen):
    if not os.path.isfile(background_save_path):
        pygame.image.save(screen,background_save_path)
        image=Image.open(background_save_path).point(lambda p: p*darken_factor)
        # image.show()
        image.save(background_save_path)
    screen.fill('black')
    background=pygame.image.load(background_save_path)
    screen.blit(background,(0,0))
    
