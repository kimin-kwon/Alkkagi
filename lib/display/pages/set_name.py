import pygame
from lib.display import input
from lib.display import dim
from lib.display.displayfunc import objects,image
from lib.display import text
from lib.display import displayfunc
from lib import delcache
import data
import hm

Screen_size=data.set.find('Screen_size')
key_pressed='a'
input.keydown=False
input.keyup=False

player_image_path=[
    hm.P1_determine.path,
    hm.P2_determine.path,
    hm.P3_determine.path,
    hm.P4_determine.path
]
kan_path='player_name_back.png'
players=hm.playernumber
button_explain_color='#555555'
max_length=8 # Set name maximum length
factor1=0.2
if players==2:
    quit_object=[
        image(kan_path,(730,150),factor1,True),
        image(kan_path,(730,250),factor1,True),
        image(player_image_path[0],(350,150),0.2),
        image(player_image_path[1],(350,250),0.2)
    ]
    texts=[
        text.Text('',70,(630,150),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,150),align='left'),
        text.Text('',70,(630,250),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,250),align='left'),
        text.Text('Press the box to enter player\'s name',100,(640,50)),
        text.Text('Player 1: ',70,(400,150),align='left'),
        text.Text('Player 2: ',70,(400,250),align='left'),
        text.Text('Enter: Start Game',30,(10,700),button_explain_color,align='left')
    ]
    player_name=['','']

elif players==3:
    quit_object=[
        image(kan_path,(730,150),factor1,True),
        image(kan_path,(730,250),factor1,True),
        image(kan_path,(730,350),factor1,True),
        image(player_image_path[0],(350,150),0.2),
        image(player_image_path[1],(350,250),0.2),
        image(player_image_path[2],(350,350),0.2)
    ]
    texts=[
        text.Text('',70,(630,150),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,150),align='left'),
        text.Text('',70,(630,250),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,250),align='left'),
        text.Text('',70,(630,350),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,350),align='left'),
        text.Text('Press the box to enter player\'s name',100,(640,50)),
        text.Text('Player 1: ',70,(400,150),align='left'),
        text.Text('Player 2: ',70,(400,250),align='left'),
        text.Text('Player 3: ',70,(400,350),align='left'),
        text.Text('Enter: Start Game',30,(10,700),button_explain_color,align='left')
    ]
    player_name=['','','']
elif players==4:
    quit_object=[
        image(kan_path,(730,150),factor1,True),
        image(kan_path,(730,250),factor1,True),
        image(kan_path,(730,350),factor1,True),
        image(kan_path,(730,450),factor1,True),
        image(player_image_path[0],(350,150),0.2),
        image(player_image_path[1],(350,250),0.2),
        image(player_image_path[2],(350,350),0.2),
        image(player_image_path[3],(350,450),0.2)
    ]
    texts=[
        text.Text('',70,(630,150),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,150),align='left'),
        text.Text('',70,(630,250),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,250),align='left'),
        text.Text('',70,(630,350),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,350),align='left'),
        text.Text('',70,(630,450),color='black',align='left',font='godoMaum'),
        text.Text(f'0/{max_length}',40,(800,450),align='left'),
        text.Text('Press the box to enter player\'s name',100,(640,50)),
        text.Text('Player 1: ',70,(400,150),align='left'),
        text.Text('Player 2: ',70,(400,250),align='left'),
        text.Text('Player 3: ',70,(400,350),align='left'),
        text.Text('Player 4: ',70,(400,450),align='left'),
        text.Text('Enter: Start Game',30,(10,700),button_explain_color,align='left')
    ]
    player_name=['','','','']
images_list=[]
texts_list=[]
clicked_text=-1
clicked=-1
temp1=-1
temp2=-1
initial_clicked=-1
mouse_pressed=False
pressed_kan=-1

def click():
    global clicked_text,clicked,quit_object,temp1,temp2,initial_clicked,mouse_pressed,pressed_kan
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
        pressed_kan=clicked # To type typing
    if input.mousedown:
        input.mousedown=False
        initial_clicked=temp1

    
        
        
            
    input.mouseup=False


clicked_size_differ=0.005
clicked_size_limit=factor1-0.01
mouse_range=0

def Screen(screen):
    global images_list,texts_list,quit_object,mouse_range
    
    screen.fill('black')
    
    pygame.draw.rect(screen,'black',(0,600,200,120))
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
        if quit_object[yo].size_mul_factor>=clicked_size_limit and quit_object[yo].button:
            quit_object[yo].size_mul_factor-=clicked_size_differ
    for i in range(len(quit_object)):
        if quit_object[i].size_mul_factor<factor1 and i!=yo and quit_object[i].button:
            quit_object[i].size_mul_factor+=clicked_size_differ
    
    # Write the player's name
    if input.keydown:
        input.keydown=False
        current_name=player_name[pressed_kan]
        if input.input_data.KeyboardInput[pygame.K_BACKSPACE]:
            current_name=current_name[:len(current_name)-1]
        elif (not input.input_data.KeyboardInput[pygame.K_RETURN]):
            try:
                if ord(key_pressed) in [32]+list(range(48,58))+list(range(65,91))+list(range(97,123)):
                    current_name=current_name+key_pressed
                if len(current_name)>max_length:
                    current_name=current_name[:len(current_name)-1]
            except:
                return
        if pressed_kan!=-1:
            player_name[pressed_kan]=current_name
            item=texts[2*pressed_kan]
            texts[2*pressed_kan]=text.Text(current_name,item.size,item.position,item.color,align=item.align)
            item2=texts[2*pressed_kan+1]
            texts[2*pressed_kan+1]=text.Text(f'{len(current_name)}/{max_length}',item2.size,item2.position,item2.color,align=item2.align)
        
    

level_determine=False
def page():
    click()
    global clicked_text,clicked,level_determine
    temp=clicked_text
    temp_image=clicked
    
    # initialize
    clicked_text=-1
    clicked=-1
    
    keyboard=input.input_data.KeyboardInput
    if keyboard[pygame.K_RETURN] and not level_determine:
        
        if '' in player_name:
            if not texts[-1].text=='Enter all player\'s names':
                texts.append(text.Text('Enter all player\'s names',100,(640,650)))
            return 'Set_name'
        level_determine=True
        if texts[-1].text=='Enter all player\'s names':
            texts[-1]=text.Text('Press Enter to start game',100,(640,650))
        else:
            texts.append(text.Text('Press Enter to start game',100,(640,650)))
        return 'Set_name'
    elif keyboard[pygame.K_RETURN] and level_determine:
        level_determine=False
        return 'Game'
    return 'Set_name'