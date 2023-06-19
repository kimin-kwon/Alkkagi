from lib.components import vector
from data.set import find
from res.loadresourcesize import size
import pygame
mu_k=find('Friction_coefficient')*40

fps=find('FPS')

#Variables defined for implementing 2d physical engine.
vdec_factor=0.5


class Rock:
    def __init__(self,position:tuple,mass:float,radius:float):
        self.position=vector.Vector(position[0],position[1])
        self.mass=mass
        self.radius=radius
    v=vector.Vector(0,0)
    outbound=False
    def move(self):
        self.position+=self.v*vdec_factor*60/fps
        # self.v*=0.9
        # if self.v.abs()<0.01:self.v*=0
        
        self.v_size=self.v.abs()
        self.temp=self.v_size**2-2*mu_k*self.v_size*vdec_factor
        # print(self.temp)
        if self.temp<0:self.temp=0
        if self.v_size!=0:self.v*=(self.temp)**0.5/self.v_size   

collision_dict={
    
}
# Sound mixer settings
# --------------------------------------------------
channel1=pygame.mixer.Channel(1)
channel1.set_volume(0.5)
sound1=pygame.mixer.Sound('Resources/Collide.mp3')
# --------------------------------------------------
def handle_exception(rock1:Rock,rock2:Rock): # This was made by the idea of R.A.
    if rock1.v*(rock2.position-rock1.position)>=0 or rock2.v*(rock1.position-rock2.position)>=0:
        return True
    else:
        return False

def isCollided(rock1:Rock, rock2:Rock):
    if (rock1.position-rock2.position).abs()<=rock1.radius+rock2.radius and handle_exception(rock1,rock2):
        channel1.play(sound1)
        return True
    else:
        return False
def handleCollision(obja:Rock,objb:Rock):
    objecta,objectb=obja,objb
    if isCollided(objecta,objectb):
        minus_a=((2*objectb.mass/(objecta.mass+objectb.mass))*((objecta.v-objectb.v)*(objecta.position-objectb.position))/(((objecta.position-objectb.position).abs())**2))*(objecta.position-objectb.position)
        minus_b=((2*objecta.mass/(objecta.mass+objectb.mass))*((objectb.v-objecta.v)*(objectb.position-objecta.position))/(((objectb.position-objecta.position).abs())**2))*(objectb.position-objecta.position)
        # minus_a=(1*((objecta.v-objectb.v)*(objecta.position-objectb.position))/((objecta.position-objectb.position)*(objecta.position-objectb.position)))*(objecta.position-objectb.position)
        # minus_b=(1*((objectb.v-objecta.v)*(objectb.position-objecta.position))/((objecta.position-objectb.position)*(objecta.position-objectb.position)))*(objectb.position-objecta.position)
        objecta.v-=minus_a
        objectb.v-=minus_b
        
    return (objecta,objectb)
    
# Not handled.
def updateposition(objects:list):
    global collision_dict
    li=objects
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if i!=j:
                collision_dict[(i,j)]=False
                li[i],li[j]=handleCollision(li[i],li[j])
    
    for i in range(len(li)):
        item=li[i]
        item.move()
        li[i]=item
        
        # Handle outbound.
        t=li[i].position
        screen_size=find('Screen_size')
        board_size=size('board.png')
        board_size_mul_factor=1.5
        x_bound=(screen_size[0]/2-board_size[0]/2*board_size_mul_factor,screen_size[0]/2+board_size[0]/2*board_size_mul_factor)
        y_bound=(screen_size[1]/2-board_size[1]/2*board_size_mul_factor,screen_size[1]/2+board_size[1]/2*board_size_mul_factor)
        if t.x<x_bound[0] or t.x>x_bound[1] or t.y<y_bound[0] or t.y>y_bound[1]:
            li[i].position=vector.Vector(100000*(i+1),100000*(i+1))
            li[i].v=vector.Vector(0,0)
            li[i].outbound=True
            
    return li
        