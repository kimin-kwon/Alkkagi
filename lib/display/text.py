import pygame
import os
pygame.init()
class Text:
    def __init__(self,text:str,size:int,position:tuple,color='white',font='godoMaum',bold=False,italic=False,align:str='center'):
        self.text=text
        self.color=color
        self.size=size
        self.align=align
        if font in pygame.font.get_fonts():
            self.font=pygame.font.SysFont(font,size,bold,italic)
        elif font+'.ttf' in os.listdir('Resources/Fonts'):
            self.font=pygame.font.Font('Resources/Fonts/'+font+'.ttf',size)
        else:
            self.font=pygame.font.Font('Resources/Fonts/ARIAL.TTF',size)
        self.object=self.font.render(self.text,True,self.color)
        self.position=position
def show(text:Text,screen):
    text_rect = text.object.get_rect()
    if text.align=='center':text_rect.center = text.position # (0,10)
    elif text.align=='left':text_rect.midleft = text.position
    elif text.align=='right':text_rect.midright = text.position
    screen.blit(text.object,text_rect)
    return (text_rect.width,text_rect.height)
def show_mul(text_list:list,screen):
    li=[]
    for item in text_list:        
        li.append(show(item,screen))
    return li
        