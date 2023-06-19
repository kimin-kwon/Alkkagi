import pygame
from lib.display import input
from lib.display import dim
from lib.display.displayfunc import objects
from lib.display import displayfunc
from lib.display import text
from lib import delcache
import data

Screen_size=data.set.find('Screen_size')

factor1=0.3
# Objects: 
quit_object=[
    displayfunc.image('exit_button.png',(500,450),factor1,True),
    displayfunc.image('cancel_button.png',(780,450),factor1,True)
]

# Set texts
texts=[
    text.Text('Are you sure you want to quit?',75,(640,250))
]

images_list=[]
texts_list=[]
quit_ind=False
cancel=False
clicked_text=0

clicked_text=-1
clicked=-1
temp1=-1
temp2=-1
initial_clicked=-1
mouse_pressed=False

def click():
    global cancel,quit_ind,clicked_text,clicked,quit_object,temp1,temp2,initial_clicked,mouse_pressed
    if input.mousedown:mouse_pressed=True
    mouse_released=input.mouseup
    mouse_position=input.input_data.MousePosition
    temp2=-1
    temp1=-1
    if mouse_pressed:
        for i in range(len(quit_object)):
            if quit_object[i].button:
                item=images_list[i]
                mouse_range=((item.position[0]-item.size[0]/2,item.position[0]+item.size[0]/2),(item.position[1]-item.size[1]/2,item.position[1]+item.size[1]/2))
                if(
                    mouse_position[0]>mouse_range[0][0] and mouse_position[0]<mouse_range[0][1] and
                    mouse_position[1]>mouse_range[1][0] and mouse_position[1]<mouse_range[1][1]
                    ):
                    temp1=i
                    break
        for j in range(len(texts_list)):
            item=texts_list[j]
            position=texts[j].position
            mouse_range=((position[0]-item[0]/2,position[0]+item[0]/2),(position[1]-item[1]/2,position[1]+item[1]/2))
            if(
                mouse_position[0]>mouse_range[0][0] and mouse_position[0]<mouse_range[0][1] and
                mouse_position[1]>mouse_range[1][0] and mouse_position[1]<mouse_range[1][1]
                ):
                temp2=j
                break
    if mouse_released and initial_clicked!=-1:
        clicked=temp1
        clicked_text=temp2
        quit_object[temp1].size_mul_factor=factor1
        temp1=-1
        temp2=-1
        mouse_pressed=False
        initial_clicked=-1
    if input.mousedown:
        input.mousedown=False
        initial_clicked=temp1
    input.mousedown=False

clicked_size_differ=0.005
clicked_size_limit=0.27
mouse_range=0

def Screen(screen):
    global images_list,texts_list,cancel,quit_object,mouse_range
    
    dim.dim_screen(screen)
    images_list=objects(quit_object,screen)
    texts_list=text.show_mul(texts,screen)
    mouse_position=input.input_data.MousePosition
    yo=-1
    for i in range(len(quit_object)):
        if quit_object[i].button:
            item=images_list[i]
            factor=factor1/(quit_object[i].size_mul_factor*2)
            mouse_range=((item.position[0]-item.size[0]*factor,item.position[0]+item.size[0]*factor),
                        (item.position[1]-item.size[1]*factor,item.position[1]+item.size[1]*factor))
            if(
                mouse_position[0]>mouse_range[0][0] and mouse_position[0]<mouse_range[0][1] and
                mouse_position[1]>mouse_range[1][0] and mouse_position[1]<mouse_range[1][1]
                ):
                yo=i
                break
    if yo!=-1 and initial_clicked!=-1:
        if quit_object[yo].size_mul_factor>=clicked_size_limit:
            quit_object[yo].size_mul_factor-=clicked_size_differ
    for i in range(len(quit_object)):
        if quit_object[i].size_mul_factor<factor1 and i!=yo:
            quit_object[i].size_mul_factor+=clicked_size_differ
def page():
    click()
    global clicked_text,clicked
    temp=clicked_text
    temp_image=clicked
    
    # initialize
    clicked_text=-1
    clicked=-1
    
    keyboard=input.input_data.KeyboardInput
    if temp_image==0:
        for i in range(len(quit_object)):
            quit_object[i].size_mul_factor=factor1
        return 'End game'
    elif keyboard[pygame.K_ESCAPE] or temp_image==1:
        delcache.delete_cache()
        for i in range(len(quit_object)):
            quit_object[i].size_mul_factor=factor1
        return 'Home'
    return 'Quit'
