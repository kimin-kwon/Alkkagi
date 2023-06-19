import pygame
import os
class Text:
    def __init__(self,text:str,size:int,color='white',font='godoMaum',bold=False,italic=False):
        if font in pygame.font.get_fonts():
            self.font=pygame.font.SysFont(font,size,bold,italic)
        elif font+'.ttf' in os.listdir('Resources/Fonts'):
            self.font=pygame.font.Font('Resources/Fonts/'+font+'.ttf',size)
        else:
            self.font=pygame.font.Font('Resources/Fonts/ARIAL.TTF',size)
        self.object=self.font.render(text,True,color)
        self.size=size
        self.size1=self.size-1
        self.size2=self.size
        self.font_str=font
        self.bold=bold
        self.italic=italic
        self.text=text
        self.color=color
    def changetextsize(self):
        if self.size1 <= self.size: 
            self.size1=self.size
            self.size += 1
            if self.size > self.size2+20 :
                self.size1=self.size+1
        elif self.size1>=self.size :
            self.size1=self.size
            self.size-=1
         
            if self.size< self.size2-20 :
                self.size1=self.size-1
        if self.font_str in pygame.font.get_fonts():
            self.font=pygame.font.SysFont(self.font_str,self.size,self.bold,self.italic)
        elif self.font_str+'.ttf' in os.listdir('Resources/Fonts'):
            self.font=pygame.font.Font('Resources/Fonts/'+self.font_str +'.ttf',self.size)
        else:
            self.font=pygame.font.Font('Resources/Fonts/ARIAL.TTF',self.size)
        self.object=self.font.render(self.text,True,self.color)
    
def show(text:Text,position:tuple or list,screen:pygame.display.set_mode):
    text_rect = text.object.get_rect()
    text_rect.center = position # (0,10)
    screen.blit(text.object,text_rect)
    return (text_rect.width,text_rect.height)
def show_mul(text_dict:dict,screen):
    li=[]
    for i in range(len(text_dict)):
        key,value=list(text_dict.items())[i]
        
        li.append(show(key,value,screen))
    return li
        
