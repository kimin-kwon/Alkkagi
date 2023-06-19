from lib.display.displayfunc import image
from lib.display.displayfunc import objects
from lib.display import input
from lib.display import text
from lib.display import images
from lib.components.vector import Vector
from lib.components import rock
import data
import math
import pygame
import hm

# Player Settings
# -----------------------------------------------------------------------------------
player_image_path=[
    hm.P1_determine.path,
    hm.P2_determine.path,
    hm.P3_determine.path,
    hm.P4_determine.path
]
player_name=[
    'Player 1',
    'Player 2',
    'Player 3',
    'Player 4'
]
players=hm.playernumber
rocks_per_player=3
# -----------------------------------------------------------------------------------

friction_coefficient=data.set.find('Friction_coefficient')

outbound_1=0
outbound_2=0
outbound_3=0
outbound_4=0
player_current=1

images_list=[]
texts_list=[]

set_score=[0 for _ in range(players)]

button_explain_color='#555555'
# Lists by players number
if players==2:
    game_object=[
        image('board.png',(640,360),1.5),
        
        image(player_image_path[0],(450,520),0.2,1),
        image(player_image_path[0],(640,520),0.4,1),
        image(player_image_path[0],(830,520),0.2,1),
        image(player_image_path[1],(450,200),0.2,1),
        image(player_image_path[1],(640,200),0.4,1),
        image(player_image_path[1],(830,200),0.2,1),
        
        image(player_image_path[0],(80,150),0.2),
        image(player_image_path[1],(80,230),0.2),
        image(player_image_path[0],(1040,150),0.2),
        
        image(player_image_path[0],(1025,380),0.2),
        image(player_image_path[1],(1025,460),0.2)
    ]
    texts=[
        text.Text(f'{player_name[player_current-1]}',50,(1085,150),'black',align='left'),
        text.Text('This turn',75,(1105,80),'black'),
        text.Text('Scores',75,(175,80),'black'),
        text.Text(f'{player_name[0]}: {3-outbound_1}',50,(125,150),'black',align='left'),
        text.Text(f'{player_name[1]}: {3-outbound_2}',50,(125,230),'black',align='left'),
        text.Text(f'{player_name[0]}: {set_score[0]}',50,(1070,380),'black',align='left'),
        text.Text(f'{player_name[1]}: {set_score[1]}',50,(1070,460),'black',align='left'),
        text.Text('Set scores',75,(1105,300),'black'),
        text.Text('F12: Screenshot',30,(10,640),button_explain_color,align='left'),
        text.Text('1: Use Mouse (Default)',30,(10,660),button_explain_color,align='left'),
        text.Text('2: Use Keyboard',30,(10,680),button_explain_color,align='left'),
        text.Text('ESC: Pause',30,(10,700),button_explain_color,align='left')
    ]

elif players==3:
    game_object=[
        image('board.png',(640,360),1.5),
        
        image(player_image_path[0],(520,570),0.2,1),
        image(player_image_path[0],(640,570),0.4,1),
        image(player_image_path[0],(760,570),0.2,1),
        image(player_image_path[1],(520,150),0.2,1),
        image(player_image_path[1],(640,150),0.4,1),
        image(player_image_path[1],(760,150),0.2,1),
        image(player_image_path[2],(430,240),0.2,1),
        image(player_image_path[2],(430,360),0.4,1),
        image(player_image_path[2],(430,480),0.2,1),
        
        image(player_image_path[0],(80,150),0.2),
        image(player_image_path[1],(80,230),0.2),
        image(player_image_path[2],(80,310),0.2),
        image(player_image_path[0],(1040,150),0.2),
        
        image(player_image_path[0],(1025,380),0.2),
        image(player_image_path[1],(1025,460),0.2),
        image(player_image_path[2],(1025,540),0.2)
    ]
    texts=[
        text.Text(f'{player_name[player_current-1]}',50,(1085,150),'black',align='left'),
        text.Text('This turn',75,(1105,80),'black'),
        text.Text('Scores',75,(175,80),'black'),
        text.Text(f'{player_name[0]}: {3-outbound_1}',50,(125,150),'black',align='left'),
        text.Text(f'{player_name[1]}: {3-outbound_2}',50,(125,230),'black',align='left'),
        text.Text(f'{player_name[2]}: {3-outbound_3}',50,(125,310),'black',align='left'),
        text.Text(f'{player_name[0]}: {set_score[0]}',50,(1070,380),'black',align='left'),
        text.Text(f'{player_name[1]}: {set_score[1]}',50,(1070,460),'black',align='left'),
        text.Text(f'{player_name[2]}: {set_score[2]}',50,(1070,540),'black',align='left'),
        text.Text('Set scores',75,(1105,300),'black'),
        text.Text('F12: Screenshot',30,(10,640),button_explain_color,align='left'),
        text.Text('1: Use Mouse (Default)',30,(10,660),button_explain_color,align='left'),
        text.Text('2: Use Keyboard',30,(10,680),button_explain_color,align='left'),
        text.Text('ESC: Pause',30,(10,700),button_explain_color,align='left')
    ]
elif players==4:
    game_object=[
        image('board.png',(640,360),1.5),
        
        image(player_image_path[0],(520,570),0.2,1),
        image(player_image_path[0],(640,570),0.4,1),
        image(player_image_path[0],(760,570),0.2,1),
        image(player_image_path[1],(520,150),0.2,1),
        image(player_image_path[1],(640,150),0.4,1),
        image(player_image_path[1],(760,150),0.2,1),
        image(player_image_path[2],(430,240),0.2,1),
        image(player_image_path[2],(430,360),0.4,1),
        image(player_image_path[2],(430,480),0.2,1),
        image(player_image_path[3],(850,240),0.2,1),
        image(player_image_path[3],(850,360),0.4,1),
        image(player_image_path[3],(850,480),0.2,1),
        
        image(player_image_path[0],(80,150),0.2),
        image(player_image_path[1],(80,230),0.2),
        image(player_image_path[2],(80,310),0.2),
        image(player_image_path[3],(80,390),0.2),
        image(player_image_path[0],(1040,150),0.2),
        
        image(player_image_path[0],(1025,380),0.2),
        image(player_image_path[1],(1025,460),0.2),
        image(player_image_path[2],(1025,540),0.2),
        image(player_image_path[3],(1025,620),0.2)
    ]
    texts=[
        text.Text(f'{player_name[player_current-1]}',50,(1085,150),'black',align='left'),
        text.Text('This turn',75,(1105,80),'black'),
        text.Text('Scores',75,(175,80),'black'),
        text.Text(f'{player_name[0]}: {3-outbound_1}',50,(125,150),'black',align='left'),
        text.Text(f'{player_name[1]}: {3-outbound_2}',50,(125,230),'black',align='left'),
        text.Text(f'{player_name[2]}: {3-outbound_3}',50,(125,310),'black',align='left'),
        text.Text(f'{player_name[3]}: {3-outbound_4}',50,(125,390),'black',align='left'),
        text.Text(f'{player_name[0]}: {set_score[0]}',50,(1070,380),'black',align='left'),
        text.Text(f'{player_name[1]}: {set_score[1]}',50,(1070,460),'black',align='left'),
        text.Text(f'{player_name[2]}: {set_score[2]}',50,(1070,540),'black',align='left'),
        text.Text(f'{player_name[3]}: {set_score[3]}',50,(1070,620),'black',align='left'),
        text.Text('Set scores',75,(1105,300),'black'),
        text.Text('F12: Screenshot',30,(10,640),button_explain_color,align='left'),
        text.Text('1: Use Mouse (Default)',30,(10,660),button_explain_color,align='left'),
        text.Text('2: Use Keyboard',30,(10,680),button_explain_color,align='left'),
        text.Text('ESC: Pause',30,(10,700),button_explain_color,align='left')
    ]

# Variables defined for implementing 2d physical engine.
index_object=0
velocity_decrease_factor=0.05 # This is factor.
maximum_power=250 # This is factor.
rock.vdec_factor=velocity_decrease_factor
initial_mouse_position=(0,0)
moved=(0,0)
vx,vy=0,0
objects_list=[
    rock.Rock(game_object[i].position,game_object[i].size_mul_factor,0) for i in range(1,players*rocks_per_player+1)
] # The len changes the number of rocks.
v_list=[0 for _ in range(players*rocks_per_player)]

end=False


moved_vec=Vector(moved[0],moved[1])


# Sound mixer settings
# --------------------------------------------------
channel2=pygame.mixer.Channel(2)
channel2.set_volume(0.5)
sound2=pygame.mixer.Sound('Resources/Throw.mp3')
# --------------------------------------------------


def drawarrow(screen,pos:tuple,arrowvector:Vector):
    head_position=(Vector(pos[0],pos[1])+arrowvector*0.5).tup()
    images.draw(images.Image('arrowhead.png',head_position,(10,10),-arrowvector.deg()),screen)
    images.draw(images.Image('arrow_line.png',pos,(arrowvector.abs(),3),-arrowvector.deg()),screen)
        


def drawarrow_mouse(screen,pos:tuple):
    
    arrowvector=moved_vec*(-0.2)
    if not input.mousedown:drawarrow(screen,pos,arrowvector)
    # pygame.draw.aaline(screen,arrowcolor,start_pos_vector.tup(),(start_pos_vector+arrowvector).tup())

def drawarrow_keyboard(screen,pos:tuple,rotAng:float=90,size:float=200):
    size*=0.2
    arrow_x=math.cos(math.radians(rotAng))
    arrow_y=math.sin(math.radians(rotAng))
    drawarrow(screen,pos,Vector(arrow_x,arrow_y)*size)
    


def move():
    global isitmoving,vx,vy,index_object,initial_mouse_position,objects_list,outbound_1,outbound_2,outbound_3,outbound_4,texts,end,change_moved,moved_vec,step,keyboard_vec,selected,rotang,arrowsize,sizedown
    
    if [outbound_1,outbound_2,outbound_3,outbound_4].count(3)==players-1:
        end=True
        return
    
    if sum([item.v.abs() for item in objects_list])==0:
        objects_list[index_object-1].v=Vector(vx,vy)
    objects_list=rock.updateposition(objects_list)
    
    n=0
    
    for index in range(players*rocks_per_player):
        item=objects_list[index]
        image_item=game_object[index+1]
        game_object[index+1]=image(
            image_item.path,item.position.tup(),image_item.size_mul_factor, # size_mul_factor is equivalent to mass.
            image_item.button)
        
        # Code to stop from repeating.
        if v_list[index]>0:n+=1
        v_list[index]=item.v.abs()
    if n!=0 and sum(v_list)==0:
        initial_mouse_position=(0,0)
        index_object=0
        vx,vy=0,0
        change_moved=True
        moved_vec=Vector(0,0)
        step=1
        keyboard_vec=Vector(0,0)
        selected=2
        rotang=90
        arrowsize=200
        sizedown=True
        if objects_list[2+(player_current-1)*3-1].outbound:
            selected=1
            if objects_list[1+(player_current-1)*3-1].outbound:
                selected=3
        
        
    
    # Show points
    outbound_1_local=0
    outbound_2_local=0
    outbound_3_local=0
    outbound_4_local=0
    for index in range(len(objects_list)):
        if index>=0 and index<rocks_per_player:
            if objects_list[index].outbound:
                outbound_1_local+=1
        if index>=rocks_per_player and index<2*rocks_per_player:
            if objects_list[index].outbound:
                outbound_2_local+=1
        if players>=3:
            if index>=2*rocks_per_player and index<3*rocks_per_player:
                if objects_list[index].outbound:
                    outbound_3_local+=1
            if players==4:
                if index>=3*rocks_per_player and index<4*rocks_per_player:
                    if objects_list[index].outbound:
                        outbound_4_local+=1
    if outbound_1_local!=outbound_1:
        pos1=texts[3]
        outbound_1=outbound_1_local
        texts[3]=text.Text(f'{player_name[0]}: {3-outbound_1}',pos1.size,pos1.position,pos1.color,align=pos1.align)
    if outbound_2_local!=outbound_2:
        pos2=texts[4]
        outbound_2=outbound_2_local
        texts[4]=text.Text(f'{player_name[1]}: {3-outbound_2}',pos2.size,pos2.position,pos2.color,align=pos2.align)
    if players>=3:
        if outbound_3_local!=outbound_3:
            pos3=texts[5]
            outbound_3=outbound_3_local
            texts[5]=text.Text(f'{player_name[2]}: {3-outbound_3}',pos3.size,pos3.position,pos3.color,align=pos3.align)
        if players==4:
            if outbound_4_local!=outbound_4:
                pos4=texts[6]
                outbound_4=outbound_4_local
                texts[6]=text.Text(f'{player_name[3]}: {3-outbound_4}',pos4.size,pos4.position,pos4.color,align=pos4.align)
    end=False
    if sum(v_list)!=0:
        isitmoving=True
    
    
keyboardinput=False
mouseinput=True

change_moved=True
frame_save=0

sound_count=0

# Keyboard input variables
selected=2
step=1
rotang=90
arrowsize=200
sizedown=True
change_player=False
isitmoving=False
keyboard_vec=(0,0)

def click(screen):
    global sound_count,isitmoving,change_player,keyboard_vec,initial_mouse_position,index_object,moved,vx,vy,player_current,moved_vec,change_moved,frame,frame_save,arrow,selected,rotang,step,arrowsize,sizedown
    
    if mouseinput:
        mouse_pressed=input.mousedown
        mouse_position=input.input_data.MousePosition
        c2=Vector(mouse_position[0],mouse_position[1])
        
        if mouse_pressed and index_object==0:
            clicked=-1
            index_list=range(rocks_per_player*(player_current-1),rocks_per_player*player_current)
            for i in index_list: # Image click
                item=images_list[1:][i]
                c1=Vector(item.position[0],item.position[1])
                
                if(
                    (c1-c2).abs()<objects_list[i].radius
                    ):
                    clicked=i
                    break
                
            if clicked!=-1:
                index_object=clicked+1
                frame_save=frame+1
        
            
        
        if index_object:
            
            if initial_mouse_position==(0,0):
                initial_mouse_position=mouse_position
            else:
                moved=(mouse_position[0]-initial_mouse_position[0],mouse_position[1]-initial_mouse_position[1])
            if change_moved:moved_vec=Vector(moved[0],moved[1])
            
            if moved_vec.abs()>250:
                temp=250/moved_vec.abs()
                moved_vec*=temp
            
                
            if input.mouseup:
                if sound_count==0:
                    channel2.play(sound2)
                    sound_count=1
                if moved_vec.abs()==0:
                    initial_mouse_position=(0,0)
                    index_object=0
                    vx,vy=0,0
                    change_moved=True
                    moved_vec=Vector(0,0)
                    step=1
                    keyboard_vec=Vector(0,0)
                    selected=2
                    rotang=90
                    arrowsize=200
                    sizedown=True
                    input.mouseup=False
                    input.mousedown=False
                    
                    return
                arrow=False
                change_moved=False
                vx,vy=(moved_vec*(-1)).tup()
                moved_vec=Vector(0,0)
                            
                # Change displayed player turn
                
        
                    
                
                    
        
        # print([item.position for item in game_object])
                
        input.mouseup=False
        input.mousedown=False
        sound_count=0
        
                
        
    
    elif keyboardinput:
        
        # Setting shoot by keyboard.
        if step==1:
            if input.keydown:
                if input.input_data.KeyboardInput[pygame.K_LEFT]:
                    if selected==2:
                        selected=1
                        if objects_list[1+(player_current-1)*3-1].outbound:
                            selected=2
                    elif selected==3:
                        selected=2
                        if objects_list[2+(player_current-1)*3-1].outbound:
                            selected=1
                            if objects_list[1+(player_current-1)*3-1].outbound:
                                selected=3
                if input.input_data.KeyboardInput[pygame.K_RIGHT]:
                    if selected==2:
                        selected=3
                        if objects_list[3+(player_current-1)*3-1].outbound:
                            selected=2
                    elif selected==1:
                        selected=2
                        if objects_list[2+(player_current-1)*3-1].outbound:
                            selected=3
                            if objects_list[1+(player_current-1)*3-1].outbound:
                                selected=1
                if input.input_data.KeyboardInput[pygame.K_RETURN]:
                    step=2
                input.keydown=False
        elif step==2:
            if input.input_data.KeyboardInput[pygame.K_LEFT]:
                rotang-=1
            elif input.input_data.KeyboardInput[pygame.K_RIGHT]:
                rotang+=1
            if input.keydown and input.input_data.KeyboardInput[pygame.K_RETURN]:
                step=3
        elif step==3:
            arrowsize_change_speed=3
            arrowsize_range=(0,250) # Sets the arrow's size range.
            if sizedown:arrowsize-=arrowsize_change_speed
            else:arrowsize+=arrowsize_change_speed
            if arrowsize<arrowsize_range[0]+arrowsize_change_speed-1:sizedown=False
            elif arrowsize==arrowsize_range[1]+1-arrowsize_change_speed:sizedown=True
            if input.keydown and input.input_data.KeyboardInput[pygame.K_RETURN]:
                step=4
            
        temp=selected+rocks_per_player*(player_current-1)
            
        selected_indicator_size_color= ('yellow', 5)    # Indicator size and color
        
        # Draw
        object_item=game_object[temp]
        
        if step<4:
            pygame.draw.circle(
                screen,
                selected_indicator_size_color[0],
                object_item.position,
                object_item.size_mul_factor*150+selected_indicator_size_color[1]
            )
            images.draw(images_list[temp],screen)
        
        if step>1 and step<4:
            if player_current==1:drawarrow_keyboard(screen,object_item.position,rotang,arrowsize*(-1))
            else:drawarrow_keyboard(screen,object_item.position,rotang,arrowsize)
        
        if step==4:
            index_object=temp
            
            if player_current==1:keyboard_vec=Vector(math.cos(math.radians(rotang)),math.sin(math.radians(rotang)))*arrowsize*(-1)
            else:keyboard_vec=Vector(math.cos(math.radians(rotang)),math.sin(math.radians(rotang)))*arrowsize
            vx,vy=keyboard_vec.tup()
            
                
        
        
        
        
        
        
        input.keydown=False
        input.keyup=False

        
    move()
    if sum(v_list)==0 and isitmoving:
        change_player=True
        isitmoving=False
        
    while change_player:
        if player_current<players:
            player_current+=1
        else:
            player_current=1
        if players==2:change_player=False
        if (players==3 and (outbound_1!=3 or outbound_2!=3 or outbound_3!=3)) or (players==4 and (outbound_1!=3 or outbound_2!=3 or outbound_3!=3 or outbound_4!=3)):
            if not ((player_current==1 and outbound_1==3) or (player_current==2 and outbound_2==3) or (player_current==3 and outbound_3==3) or (players==4 and player_current==4 and outbound_4==3)):
                change_player=False
    # Show current turn.
    text_item=texts[0]
    text_item.text = f'{player_name[player_current-1]}'
    text_item.object=text_item.font.render(text_item.text,True,text_item.color)
    image_item=game_object[1+players*(rocks_per_player+1)]
    image_item.path=player_image_path[player_current-1]
    game_object[1+players*(rocks_per_player+1)]=image_item
    
        
        
    
frame=0
arrow=False

def Screen(screen):
    global images_list,texts_list,end,moved_vec,frame,arrow,frame_save,mouseinput,keyboardinput,step,texts
    
    # Refresh
    if players==2:
        texts=[
            text.Text(f'{player_name[player_current-1]}',50,(1085,150),'black',align='left'),
            text.Text('This turn',75,(1105,80),'black'),
            text.Text('Scores',75,(175,80),'black'),
            text.Text(f'{player_name[0]}: {3-outbound_1}',50,(125,150),'black',align='left'),
            text.Text(f'{player_name[1]}: {3-outbound_2}',50,(125,230),'black',align='left'),
            text.Text(f'{player_name[0]}: {set_score[0]}',50,(1070,380),'black',align='left'),
            text.Text(f'{player_name[1]}: {set_score[1]}',50,(1070,460),'black',align='left'),
            text.Text('Set scores',75,(1105,300),'black'),
            text.Text('F12: Screenshot',30,(10,640),button_explain_color,align='left'),
            text.Text('1: Use Mouse (Default)',30,(10,660),button_explain_color,align='left'),
            text.Text('2: Use Keyboard',30,(10,680),button_explain_color,align='left'),
            text.Text('ESC: Pause',30,(10,700),button_explain_color,align='left')
        ]
    elif players==3:
        texts=[
            text.Text(f'{player_name[player_current-1]}',50,(1085,150),'black',align='left'),
            text.Text('This turn',75,(1105,80),'black'),
            text.Text('Scores',75,(175,80),'black'),
            text.Text(f'{player_name[0]}: {3-outbound_1}',50,(125,150),'black',align='left'),
            text.Text(f'{player_name[1]}: {3-outbound_2}',50,(125,230),'black',align='left'),
            text.Text(f'{player_name[2]}: {3-outbound_3}',50,(125,310),'black',align='left'),
            text.Text(f'{player_name[0]}: {set_score[0]}',50,(1070,380),'black',align='left'),
            text.Text(f'{player_name[1]}: {set_score[1]}',50,(1070,460),'black',align='left'),
            text.Text(f'{player_name[2]}: {set_score[2]}',50,(1070,540),'black',align='left'),
            text.Text('Set scores',75,(1105,300),'black'),
            text.Text('F12: Screenshot',30,(10,640),button_explain_color,align='left'),
            text.Text('1: Use Mouse (Default)',30,(10,660),button_explain_color,align='left'),
            text.Text('2: Use Keyboard',30,(10,680),button_explain_color,align='left'),
            text.Text('ESC: Pause',30,(10,700),button_explain_color,align='left')
        ]
    elif players==4:
        texts=[
            text.Text(f'{player_name[player_current-1]}',50,(1085,150),'black',align='left'),
            text.Text('This turn',75,(1105,80),'black'),
            text.Text('Scores',75,(175,80),'black'),
            text.Text(f'{player_name[0]}: {3-outbound_1}',50,(125,150),'black',align='left'),
            text.Text(f'{player_name[1]}: {3-outbound_2}',50,(125,230),'black',align='left'),
            text.Text(f'{player_name[2]}: {3-outbound_3}',50,(125,310),'black',align='left'),
            text.Text(f'{player_name[3]}: {3-outbound_4}',50,(125,390),'black',align='left'),
            text.Text(f'{player_name[0]}: {set_score[0]}',50,(1070,380),'black',align='left'),
            text.Text(f'{player_name[1]}: {set_score[1]}',50,(1070,460),'black',align='left'),
            text.Text(f'{player_name[2]}: {set_score[2]}',50,(1070,540),'black',align='left'),
            text.Text(f'{player_name[3]}: {set_score[3]}',50,(1070,620),'black',align='left'),
            text.Text('Set scores',75,(1105,300),'black'),
            text.Text('F12: Screenshot',30,(10,640),button_explain_color,align='left'),
            text.Text('1: Use Mouse (Default)',30,(10,660),button_explain_color,align='left'),
            text.Text('2: Use Keyboard',30,(10,680),button_explain_color,align='left'),
            text.Text('ESC: Pause',30,(10,700),button_explain_color,align='left')
        ]
    screen.fill('black')
    
    for i in range(players):
        pos=texts[3+players+i]
        texts[3+players+i]=text.Text(f'{player_name[i]}: {set_score[i]}',pos.size,pos.position,pos.color,align=pos.align)
    
    pygame.draw.rect(screen,'#aaaaaa',(30,30,280,120+80*players),0,30)
    pygame.draw.rect(screen,'#aaaaaa',(970,30,280,200),0,30)
    pygame.draw.rect(screen,'#aaaaaa',(970,250,280,120+80*players),0,30)
    
    images_list=objects(game_object,screen)
    if input.input_data.KeyboardInput[pygame.K_1] and index_object==0:mouseinput=True;keyboardinput=False
    elif input.input_data.KeyboardInput[pygame.K_2] and index_object==0:mouseinput=False;keyboardinput=True;step=1
    
    for i in range(len(objects_list)):
        objects_list[i].radius=images_list[1:][i].size[0]/2
    
    texts_list=text.show_mul(texts,screen)
    
    # Handle arrow flicking.
    frame=(frame+1)%3
    if frame_save!=0 and (frame-frame_save in [1,-2]):
        arrow=True
        frame_save=0
    if arrow and moved_vec.abs()!=0: drawarrow_mouse(screen,objects_list[index_object-1].position.tup())
        
        
    click(screen)
    
    
def page():
    keyboard=input.input_data.KeyboardInput
    # if keyboard[pygame.K_SPACE]:return 'Idle'
    if keyboard[pygame.K_ESCAPE]:
        return 'Pause'
    if end:
        return 'End'
    return 'Game'
    
    