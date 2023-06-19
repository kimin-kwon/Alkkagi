from lib.display import text
from lib.display import dim
from lib.display import input
from lib.display.displayfunc import objects
from lib.components.vector import Vector
from lib import delcache
import logging
import copy
import pygame

winner=0
places=[]
names=[]
score=(0,0)
game_number=0
sets=0
set_score=[]

# Sound mixer settings
# --------------------------------------------------
channel3=pygame.mixer.Channel(3)
channel3.set_volume(0.5)
sound3=pygame.mixer.Sound('Resources/end.mp3')
# --------------------------------------------------

game_object=[
    
]
texts=[]
players=2
posit=[1085,1000] # Position of set score display at end screen
def define_texts(players):
    global texts,posit
    if game_number<sets:
        item=text.Text('Next game',70,(400,500))
    else:
        item=text.Text('Continue',70,(400,500))
        # posit=[100000,100000]
    if players==2:
        texts=[
            text.Text(f'Winner: {names[winner]}',70,(640,300)),
            text.Text(f'{score[0]}:{score[1]}',70,(640,400)),
            item,
            text.Text('Home',70,(880,500)),
            text.Text('Set scores',50,(posit[0],100)),
            text.Text(names[0]+': '+str(set_score[0]),50,(posit[1],180),align='left'),
            text.Text(names[1]+': '+str(set_score[1]),50,(posit[1],260),align='left')
        ]
    elif players == 3:
        texts=[
            text.Text(f'1st place: {names[winner]}',70,(640,200)),
            text.Text(f'2nd place: {names[places[1]]}',70,(640,300)),
            text.Text(f'3rd place: {names[places[2]]}',70,(640,400)),
            item,
            text.Text('Home',70,(880,500)),
            text.Text('Set scores',50,(posit[0],100)),
            text.Text(names[0]+': '+str(set_score[0]),50,(posit[1],180),align='left'),
            text.Text(names[1]+': '+str(set_score[1]),50,(posit[1],260),align='left'),
            text.Text(names[2]+': '+str(set_score[2]),50,(posit[1],340),align='left')
        ]
    elif players == 4:
        texts=[
            text.Text(f'1st place: {names[winner]}',70,(640,100)),
            text.Text(f'2nd place: {names[places[1]]}',70,(640,200)),
            text.Text(f'3rd place: {names[places[2]]}',70,(640,300)),
            text.Text(f'4th place: {names[places[3]]}',70,(640,400)),
            item,
            text.Text('Home',70,(880,500)),
            text.Text('Set scores',50,(posit[0],100)),
            text.Text(names[0]+': '+str(set_score[0]),50,(posit[1],180),align='left'),
            text.Text(names[1]+': '+str(set_score[1]),50,(posit[1],260),align='left'),
            text.Text(names[2]+': '+str(set_score[2]),50,(posit[1],340),align='left'),
            text.Text(names[3]+': '+str(set_score[3]),50,(posit[1],420),align='left')
        ]

def define_texts_final(players):
    global texts,posit
    if game_number<sets:
        item=text.Text('Next game',70,(400,500))
    else:
        item=text.Text('Play again',70,(400,500))
        # posit=[100000,100000]
    
    add_texts=True
    n=0
    i=0
    texts=[item,text.Text('Home',70,(880,500))]
    while add_texts:
        if i==0:
            prefix='1st place: '
        elif i==1:
            prefix='2nd place: '
        elif i==2:
            prefix='3rd place: '
        elif i==3:
            prefix='4th place: '
        texts.append(text.Text(prefix+final_places[i],70,(640,420-80*(len(final_places)-i))))
        n+=len(list(final_places[i].split('and')))
        i+=1
        if n==players:break
    if i==1:
        prefix='Both '
        if players>=3:prefix='All '
        texts=[
            item,text.Text('Home',70,(880,500)),
            text.Text('Tied! '+prefix+final_places[0].split(', ')[-1],70,(640,420-80*(len(final_places))))
        ]
        
        

images_list=[]
texts_list=[]

# Variables for displaying final set scores
end_final=False
final_places=[]

clicked_object='End'
def click():
    global clicked_object
    
    mouse_pressed=input.mousedown
    mouse_position=input.input_data.MousePosition
    input.mousedown=False
    input.mouseup=False
    if mouse_pressed:
        index=0
        for index in range(len(texts_list)):
            text_position=Vector(texts[index].position[0],texts[index].position[1])
            text_size=Vector(texts_list[index][0],texts_list[index][1])
            mouse_range=(
                text_position-text_size/2,
                text_position+text_size/2
            )
            if mouse_position[0]>mouse_range[0].tup()[0] and mouse_position[0]<mouse_range[1].tup()[0] and mouse_position[1]>mouse_range[0].tup()[1] and mouse_position[1]<mouse_range[1].tup()[1]:
                break
        if index==players and game_number<sets:clicked_object='Next Game'
        elif index==players and game_number==sets and not change_button:clicked_object='Continue'
        elif index==0 and game_number==sets and change_button:clicked_object='Play again'
        elif (index==players+1 and not change_button) or (index==1 and change_button):clicked_object='Home'
    
gamerecordsaved=False # A variable for writing one log per game.
def savegamerecord():
    global gamerecordsaved
    log_path='data/log/game_log.txt'
    
    logging.basicConfig(filename=log_path,format='%(asctime)s - %(message)s',level=logging.INFO,datefmt='%b %d, %Y, %H:%M:%S')
    logging.info(' '.join([names[i]+': '+str(score[i]) for i in places[::-1]])+f', Set={game_number}/{sets}')
    gamerecordsaved=True
    

defined=True
change_button=False
music_played=False
def Screen(screen):
    global music_played
    if not music_played:
        channel3.play(sound3)
        music_played=True
    global texts_list,images_list,texts,final_places,clicked_object,end_final,defined,change_button
    dim.dim_screen(screen)
    images_list=objects(game_object,screen)
    
    if not end_final and defined:
        define_texts(players) # Show places
        defined=False
    
    # At the end of sets, show final set scores
    if end_final:
        set_score_copy=copy.deepcopy(set_score)
        i=0
        final_places=[]
        while i<players:
            max_value=max(set_score_copy)
            same_place_num=set_score_copy.count(max_value)
            the_list=[]
            for _ in range(same_place_num):
                new_index=set_score_copy.index(max_value)
                the_list.append(names[new_index])
                set_score_copy[new_index]=0
            final_places.append(' and '.join(the_list)+f', {max_value}pts')
            i+=same_place_num
        # print(', '.join(final_places))
        end_final=False
        change_button=True
        clicked_object='End'
        define_texts_final(players)
    # score=(0,0)
    
    
    if score==(0,0): # Handle unexpected tie.
        texts[0]=text.Text('Tied!',texts[0].size,texts[0].position)
        for i in range(1,players):
            texts[i]=text.Text('',0,(0,0))
    
    
    texts_list=text.show_mul(texts,screen)
    if gamerecordsaved==False:savegamerecord() # Save result to log.

idlereset=False
def initialize_page(page):
    global idlereset,clicked_object,end_final,defined,change_button,set_score,music_played
    if page in ['Next Game','Play again','Home']:
        clicked_object='End'
        defined=True
        change_button=False
        music_played=False
        delcache.delete_cache()
    if page in ['Play again','Home']:
        end_final=False
        set_score=[]
        idlereset=True
set_score_reset=False
def page():
    global clicked_object,end_final,defined,set_score,set_score_reset,music_played
    click()
    if clicked_object=='End':
        return 'End'
    elif clicked_object=='Continue':
        end_final=True
        return 'End'
    elif clicked_object=='Next Game':
        initialize_page(clicked_object)
        return 'Game'
    elif clicked_object=='Play again':
        initialize_page(clicked_object)
        set_score_reset=True
        return 'Idle'
    elif clicked_object=='Home':
        initialize_page(clicked_object)
        set_score_reset=True
        return 'Home'