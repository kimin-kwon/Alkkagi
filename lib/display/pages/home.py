from lib.display import displayfunc
from lib.display import text
from lib.display.input import input_data
import pygame

# Objects
home_object=[
    displayfunc.image('Title.png',(640,180)),
    # displayfunc.image('Home_announcement.png',(640,540))
]

button_explain_color='#555555'
texts=[
    text.Text('Press Enter to start',150,(640,540)),
    text.Text('F12: Screenshot',30,(10,660),button_explain_color,align='left'),
    text.Text('F1: Settings',30,(10,680),button_explain_color,align='left'),
    text.Text('ESC: Quit',30,(10,700),button_explain_color,align='left')
]

images_list=[]
texts_list=[]

def Screen(screen):
    global images_list,texts_list
    screen.fill('black')
    images_list=displayfunc.objects(home_object,screen)
    texts_list=text.show_mul(texts,screen)
def page():
    keyboard=input_data.KeyboardInput
    # if keyboard[pygame.K_SPACE]:return 'Idle'
    if keyboard[pygame.K_RETURN]:return 'Idle'
    elif keyboard[pygame.K_F1]:return 'Settings'
    elif keyboard[pygame.K_ESCAPE]:return 'Quit'
    return 'Home'
    
    