import pygame
import data

class input_data_class:
    def __init__(self,KeyboardInput:list,MouseDown:bool=False,MousePosition:list=[i/2 for i in data.set.find('Screen_size')]):
        self.MouseDown=MouseDown
        self.MousePosition=MousePosition
        self.KeyboardInput=KeyboardInput

input_data=input_data_class(KeyboardInput=[])
mousedown=False
mouseup=False
keydown=False
keyup=False
def inputdetect():
    global input_data
    input_data.MouseDown=pygame.mouse.get_pressed()
    input_data.KeyboardInput=pygame.key.get_pressed()
    input_data.MousePosition=pygame.mouse.get_pos()