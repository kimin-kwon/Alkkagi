import pygame
from lib.display.input import input_data
from lib.display import dim
from lib.display import displayfunc
from lib.display import text
from lib.display import input
from lib import delcache
import data

# Settings
fps=int(data.set.find('FPS'))
volume1=int(data.set.find('Volume_song'))
volume2=int(data.set.find('Volume_effect'))

factor1=0.4
# Objects
settings_object=[
    displayfunc.image('rightarrow.png',(825,216),factor1,button=True),
    displayfunc.image('leftarrow.png',(675,216),factor1,button=True),
    displayfunc.image('rightarrow.png',(825,296),factor1,button=True),
    displayfunc.image('leftarrow.png',(675,296),factor1,button=True),
    displayfunc.image('rightarrow.png',(825,376),factor1,button=True),
    displayfunc.image('leftarrow.png',(675,376),factor1,button=True)
]

# Set texts
texts=[
    text.Text(str(fps),70,(750,216)),
    text.Text('FPS',80,(600,216),align='right'),
    text.Text(str(volume1),70,(750,296)),
    text.Text('Music Volume',80,(600,296),align='right'),
    text.Text(str(volume2),70,(750,376)),
    text.Text('Effect Volume',80,(600,376),align='right')
]

images_list=[]
texts_list=[]
fps_list=[30,60,75,120,144,165,240,300,360]
fps_index=fps_list.index(fps)
clicked=-1
temp1=-1
temp2=-1
initial_clicked=-1
mouse_pressed=False

def click():
    global fps,fps_index,clicked,clicked,settings_object,temp1,temp2,initial_clicked,mouse_pressed,volume1,volume2
    if input.mousedown:mouse_pressed=True
    mouse_released=input.mouseup
    mouse_position=input_data.MousePosition
    temp1=-1
    temp2=-1
    if mouse_pressed:
        for i in range(len(settings_object)):
            if settings_object[i].button:
                item=images_list[i]
                mouse_range=((item.position[0]-item.size[0]/2,item.position[0]+item.size[0]/2),(item.position[1]-item.size[1]/2,item.position[1]+item.size[1]/2))
                if(
                    mouse_position[0]>mouse_range[0][0] and mouse_position[0]<mouse_range[0][1] and
                    mouse_position[1]>mouse_range[1][0] and mouse_position[1]<mouse_range[1][1]
                    ):
                    temp1=i
                    break
    if mouse_released and initial_clicked!=-1:
        clicked=temp1
        settings_object[temp1].size_mul_factor=factor1
        temp1=-1
        temp2=-1
        mouse_pressed=False
        initial_clicked=-1
        if clicked==0: # fps increase
            fps_position=texts[0].position
            fps_index+=1
            if fps_index==len(fps_list):fps_index-=1
            fps=fps_list[fps_index]
            data.set.change('FPS',fps)
            texts[0]=(text.Text(str(fps),70,fps_position))
        if clicked==1: # fps decrease
            fps_position=texts[0].position
            fps_index-=1
            if fps_index==-1:fps_index+=1
            fps=fps_list[fps_index]
            data.set.change('FPS',fps)
            texts[0]=(text.Text(str(fps),70,fps_position))
        if clicked==2: # Music volume increase
            volume1_position=texts[2].position
            volume1+=1
            if volume1==101:volume1-=1
            data.set.change('Volume_song',volume1)
            texts[2]=(text.Text(str(volume1),70,volume1_position))
        if clicked==3: # Music volume decrease
            volume1_position=texts[2].position
            volume1-=1
            if volume1==-1:volume1+=1
            data.set.change('Volume_song',volume1)
            texts[2]=(text.Text(str(volume1),70,volume1_position))
        if clicked==4: # SFX volume increase
            volume2_position=texts[4].position
            volume2+=1
            if volume2==101:volume2-=1
            data.set.change('Volume_effect',volume2)
            texts[4]=(text.Text(str(volume2),70,volume2_position))
        if clicked==5: # SFX volume decrease
            volume2_position=texts[4].position
            volume2-=1
            if volume2==-1:volume2+=1
            data.set.change('Volume_effect',volume2)
            texts[4]=(text.Text(str(volume2),70,volume2_position))
        clicked=-1
    if input.mousedown:
        input.mousedown=False
        initial_clicked=temp1
    input.mouseup=False
    
clicked_size_differ=0.005
clicked_size_limit=0.37
mouse_range=0
             

def Screen(screen):
    global images_list,settings_object,mouse_range
    dim.dim_screen(screen)
    images_list=displayfunc.objects(settings_object,screen)
    text.show_mul(texts,screen)
    mouse_position=input.input_data.MousePosition
    yo=-1
    for i in range(len(settings_object)):
        if settings_object[i].button:
            item=images_list[i]
            factor=factor1/(settings_object[i].size_mul_factor*2)
            mouse_range=((item.position[0]-item.size[0]*factor,item.position[0]+item.size[0]*factor),
                         (item.position[1]-item.size[1]*factor,item.position[1]+item.size[1]*factor))
            if(
                mouse_position[0]>mouse_range[0][0] and mouse_position[0]<mouse_range[0][1] and
                mouse_position[1]>mouse_range[1][0] and mouse_position[1]<mouse_range[1][1]
                ):
                yo=i
                break
    if yo!=-1 and initial_clicked!=-1:
        if settings_object[yo].size_mul_factor>=clicked_size_limit:
            settings_object[yo].size_mul_factor-=clicked_size_differ
    for i in range(len(settings_object)):
        if settings_object[i].size_mul_factor<factor1 and i!=yo:
            settings_object[i].size_mul_factor+=clicked_size_differ
    input.keydown=False
    
def page():
    click()
    global clicked
    clicked=-1
    keyboard=input_data.KeyboardInput
    if keyboard[pygame.K_ESCAPE]:
        for i in range(len(settings_object)):
            settings_object[i].size_mul_factor=factor1
        delcache.delete_cache()
        return 'Home'
    return 'Settings'
def page_ingame():
    click()
    keyboard=input_data.KeyboardInput
    if keyboard[pygame.K_ESCAPE]:
        for i in range(len(settings_object)):
            settings_object[i].size_mul_factor=factor1
        return 'Pause'
    return 'Settings_ingame'