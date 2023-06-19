import pygame
pygame.init()
class Image:
    def __init__(self,path:str,position:tuple,size:tuple,rotAng=0): # rotAng is CCW
        self.item=pygame.image.load('Resources/'+path)
        self.item=self.item.convert_alpha()
        self.position,self.size,self.angle=position,size,rotAng

def draw(arg:Image,screen):
    if not arg.__class__.__name__=='Image':return
    img=pygame.transform.scale(arg.item,arg.size)
    if arg.angle!=0:
        img=pygame.transform.rotate(img,arg.angle)
    img_rect=img.get_rect()
    img_rect.center=arg.position
    screen.blit(img,img_rect)